# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: hist.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 4/1/23 22:56
"""
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def get_letter(num):
    return chr(num + 64)


WELL_NAME = 'QCWell'  # QCWell or CountedWell
PLOT_PARAM = 'Size'  # Circularity, Size, MeanIntensity, MaxIntensity, or TotalIntensity

# Read in the ELISpot data
tree = ET.parse('data/042221_CLP_IL7_heme_for_nanostring.xml')
root = tree.getroot()

# Set up the plot
fig, axs = plt.subplots(nrows=8, ncols=12, figsize=(48, 32), gridspec_kw={'hspace': 0.2, 'wspace': 0.2})
fig.suptitle(f'ELISpot {root.find("./PlateName").text}', fontsize=45)

# Loop through each well in the ELISpot data
for well in root.findall(f'.//{WELL_NAME}'):

    # Get the well's row and column number
    row = int(well.find('./Row').text)
    col = int(well.find('./Column').text)
    spot_count = int(well.find('./WellResult/ActualSpotCount').text)
    print(f'Well {get_letter(row)},{col}, {spot_count}')

    # Create a subplot for the well
    ax = axs[row - 1, col - 1]

    # Get the well's spot data
    spot_list = well.findall('./WellResult/Spot_List/Spot')
    # Plot each spot in the well
    intensity_list = []
    for spot in spot_list:
        intensity_list.append(float(spot.find(f'./{PLOT_PARAM}').text))
    ax.hist(intensity_list, bins=30, color='blue')
    ax.set_title(f'{get_letter(row)}{col}, {spot_count}', loc='right')

# Add x and y axis labels
fig.text(0.5, 0.02, PLOT_PARAM, ha='center', fontsize=40)
fig.text(0.01, 0.5, 'Frequency', va='center', rotation='vertical', fontsize=40)
fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.93)

# add row numbers on the left side of the grid
for i, ax in enumerate(axs[:, 0]):
    ax.annotate(f"{get_letter(i+1)}", xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - 5, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                ha='right', va='center', fontsize=50)

# add column numbers on the top of the grid
for i, ax in enumerate(axs[0, :]):
    ax.annotate(f"{i+1}", xy=(0.5, 1), xytext=(0, ax.xaxis.labelpad + 5),
                xycoords='axes fraction', textcoords='offset points'
                , ha='center', va='baseline', fontsize=50)
# Show the plot
plt.show()
