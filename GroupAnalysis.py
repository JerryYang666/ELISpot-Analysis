# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: GroupAnalysis.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 4/27/23 22:54
"""
import numpy as np
import matplotlib.pyplot as plt

from GetDataFromXML import GetDataFromXML


def closest_factors(n):
    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0:
            return i, n // i


def remove_outliers(data, m=3):
    """
    delete the outlier in the data
    :param data: a list of data
    :param m: the number of standard deviation away from the mean
    :return: a list of data without outlier
    """
    data = np.array(data)
    mean = np.mean(data)
    std = np.std(data)
    data = data[np.abs(data - mean) < m * std]
    return data


class GroupAnalysis:

    def __init__(self, group_dict, file_path, well_name='QCWell'):
        self.group_dict = group_dict  # e.g. {'group1': ['A1', 'A2'], 'group2': ['A3', 'A4']}
        self.file_path = file_path
        self.well_name = well_name
        self.data_source = GetDataFromXML(self.file_path, self.well_name)

    def one_group_aggregation(self, group_name, plot_param, remove_outlier=False):
        """
        aggregate the data from all wells in one group to a single list for each plot_param
        :param remove_outlier: whether to remove the outlier, default is False
        :param group_name: name of the group, e.g. 'group1'
        :param plot_param: a list of plot parameters, e.g. ['MeanIntensity', 'Size']
        :return: a dictionary of aggregated data for each plot_param e.g. {'MeanIntensity': np.array(), 'Size': np.array()}
        """
        if group_name in self.group_dict:
            data = self.data_source.get_data(self.group_dict[group_name], plot_param=plot_param)
            aggregated_data = {}
            for param in plot_param:
                aggregated_data[param] = np.array([])
                for well in data:
                    preprocessed = data[well][param]
                    if remove_outlier:
                        preprocessed = remove_outliers(preprocessed)
                    aggregated_data[param] = np.append(aggregated_data[param], preprocessed)
            return aggregated_data
        else:
            return 'Group name not found'

    def all_group_aggregation(self, plot_param):
        """
        aggregate the data from all wells in all groups to a single list for each plot_param
        :param plot_param: a list of plot parameters, e.g. ['MeanIntensity', 'Size']
        :return: a dictionary of aggregated data for each plot_param
        e.g. {'group1': {'MeanIntensity': np.array(), 'Size': np.array()}, 'group2': {'MeanIntensity': np.array(), 'Size': np.array()}}
        """
        all_aggregated_data = {}
        for group_name in self.group_dict:
            group_data = self.one_group_aggregation(group_name, plot_param)
            all_aggregated_data[group_name] = group_data
        return all_aggregated_data

    def aggregation_histogram_analysis(self, one_plot_param):
        """
        plot the histogram of the aggregated data on one plot_param
        :return:
        """
        # get the number of rows and columns for the subplot
        subplot_row, subplot_col = closest_factors(len(self.group_dict))
        # Set up the plot
        fig, axs = plt.subplots(nrows=subplot_row, ncols=subplot_col,
                                figsize=(subplot_col * 4, subplot_row * 4),
                                gridspec_kw={'hspace': 0.2, 'wspace': 0.2})
        fig.suptitle(f'ELISpot {self.file_path}')
        group_no = 0
        for i in range(0, subplot_row):
            for j in range(0, subplot_col):
                group_name = list(self.group_dict.keys())[group_no]
                group_data = self.one_group_aggregation(group_name, [one_plot_param])
                if subplot_row == 1 or subplot_col == 1:
                    axs[group_no].hist(group_data[one_plot_param], bins=30)
                    axs[group_no].set_title(f'{group_name}, {len(group_data[one_plot_param])}')
                    # set x axis range
                    axs[group_no].set_xlim([0, 80000])
                else:
                    axs[i, j].hist(group_data[one_plot_param], bins=30)
                    axs[i, j].set_title(f'{group_name}, {len(group_data[one_plot_param])}')
                    # set x axis range
                    axs[i, j].set_xlim([0, 80000])
                group_no += 1
        fig.text(0.5, 0.02, one_plot_param, ha='center')
        fig.text(0.04, 0.5, 'Frequency', va='center', rotation='vertical')
        plt.show()


"""
gp = GroupAnalysis({'Naive-IFNg': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2'],
                    'CLP+HemeVehicle-IFNg': ['E1', 'E2', 'F1', 'F2', 'G1', 'G2', 'H1', 'H2', 'A3', 'A4'],
                    'CLP+Heme-IFNg': ['B3', 'B4', 'C3', 'C4', 'D3', 'D4', 'E3', 'E4', 'F3', 'F4'],
                    'CLP+PBS-IFNg': ['G3', 'G4', 'H3', 'H4', 'A5', 'A6', 'B5', 'B6', 'C5', 'C6'],
                    'CLP+IL7-IFNg': ['D5', 'D6', 'E5', 'E6', 'F5', 'F6', 'G5', 'G6', 'H5', 'H6'],
                    'Naive-TNFa': ['A7', 'A8', 'B7', 'B8', 'C7', 'C8', 'D7', 'D8'],
                    'CLP+HemeVehicle-TNFa': ['E7', 'E8', 'F7', 'F8', 'G7', 'G8', 'H7', 'H8', 'A9', 'A10'],
                    'CLP+Heme-TNFa': ['B9', 'B10', 'C9', 'C10', 'D9', 'D10', 'E9', 'E10', 'F9', 'F10'],
                    'CLP+PBS-TNFa': ['G9', 'G10', 'H9', 'H10', 'A11', 'A12', 'B11', 'B12', 'C11', 'C12'],
                    'CLP+IL7-TNFa': ['D11', 'D12', 'E11', 'E12', 'F11', 'F12', 'G11', 'G12', 'H11', 'H12']},
                   'data/042221_CLP_IL7_heme_for_nanostring.xml')
"""
# print(gp.one_group_aggregation('group1', ['MeanIntensity']))
# x = gp.all_group_aggregation(['MeanIntensity', 'Size'])
# gp.aggregation_histogram_analysis('MeanIntensity')
# gp.aggregation_histogram_analysis('Size')
