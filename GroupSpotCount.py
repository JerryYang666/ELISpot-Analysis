# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: GroupSpotCount.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 12/1/23 20:23
"""
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


class GroupSpotCount:
    def __init__(self, group_dict, file_path):
        self.group_dict = group_dict
        self.file_path = file_path
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()

    def one_group_aggregation(self, group_name):
        if group_name in self.group_dict:
            group_data = []
            for well in self.root.findall('.//QCWell'):
                row = well.find('./Row').text
                col = well.find('./Column').text
                well_name = chr(int(row) + 64) + col
                if well_name in self.group_dict[group_name]:
                    spot_count = int(well.find('./WellResult/ActualSpotCount').text)
                    group_data.append(spot_count)
            return group_data
        else:
            return 'Group name not found'

    def all_group_aggregation(self):
        all_group_data = {}
        max_length = 0
        for group_name in self.group_dict:
            group_data = self.one_group_aggregation(group_name)
            max_length = max(max_length, len(group_data))
            all_group_data[group_name] = group_data

        # Convert to float and pad shorter lists with np.nan
        for group_name, group_data in all_group_data.items():
            group_data = np.array(group_data, dtype=float)  # Convert to float
            if len(group_data) < max_length:
                all_group_data[group_name] = np.pad(
                    group_data, (0, max_length - len(group_data)), constant_values=np.nan
                )

        return all_group_data


groups = {'Naive-IFNg': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2'],
            'CLP+HemeVehicle-IFNg': ['E1', 'E2', 'F1', 'F2', 'G1', 'G2', 'H1', 'H2', 'A3', 'A4'],
            'CLP+Heme-IFNg': ['B3', 'B4', 'C3', 'C4', 'D3', 'D4', 'E3', 'E4', 'F3', 'F4'],
            'CLP+PBS-IFNg': ['G3', 'G4', 'H3', 'H4', 'A5', 'A6', 'B5', 'B6', 'C5', 'C6'],
            'CLP+IL7-IFNg': ['D5', 'D6', 'E5', 'E6', 'F5', 'F6', 'G5', 'G6', 'H5', 'H6'],
            'Naive-TNFa': ['A7', 'A8', 'B7', 'B8', 'C7', 'C8', 'D7', 'D8'],
            'CLP+HemeVehicle-TNFa': ['E7', 'E8', 'F7', 'F8', 'G7', 'G8', 'H7', 'H8', 'A9', 'A10'],
            'CLP+Heme-TNFa': ['B9', 'B10', 'C9', 'C10', 'D9', 'D10', 'E9', 'E10', 'F9', 'F10'],
            'CLP+PBS-TNFa': ['G9', 'G10', 'H9', 'H10', 'A11', 'A12', 'B11', 'B12', 'C11', 'C12'],
            'CLP+IL7-TNFa': ['D11', 'D12', 'E11', 'E12', 'F11', 'F12', 'G11', 'G12', 'H11', 'H12']}

group_spot_count = GroupSpotCount(groups, 'data/042221_CLP_IL7_heme_for_nanostring.xml')
group_data = group_spot_count.all_group_aggregation()

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(group_data)

# Melt the DataFrame to a long format
df_melt = df.melt(var_name='Group', value_name='ActualSpotCount')

# List of groups to plot
groups_to_plot = ['Naive-IFNg', 'CLP+PBS-IFNg', 'Naive-TNFa', 'CLP+PBS-TNFa']

# Create a new list with 'PBS' removed from the group names
new_group_names = [group.replace('+PBS', '') for group in groups_to_plot]

# Filter the DataFrame to include only the specified groups
df_melt_filtered = df_melt[df_melt['Group'].isin(groups_to_plot)]

# Create the box and whisker plot for the filtered data
plt.figure(figsize=(5, 5))
sns.boxplot(x='Group', y='ActualSpotCount', data=df_melt_filtered)
# Set the x-axis labels to the new group names
plt.xticks(range(len(new_group_names)), new_group_names, rotation=45)

plt.subplots_adjust(bottom=0.2)
plt.subplots_adjust(top=0.98)
plt.show()