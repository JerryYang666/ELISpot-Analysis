# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: GetDataFromXML.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 4/27/23 22:11
"""
import xml.etree.ElementTree as ET
import numpy as np


def get_letter(num):
    return chr(num + 64)


class GetDataFromXML:
    def __init__(self, xml_path, well_name='QCWell'):
        self.xml_path = xml_path
        self.well_name = well_name
        # Read in the ELISpot data
        tree = ET.parse(self.xml_path)
        self.root = tree.getroot()

    def get_data(self, well_num=None, plot_param=None):
        """
        Get the data from the ELISpot xml file
        :param well_num: a list of well numbers, e.g. ['A1', 'A2']
        :param plot_param: a list of plot parameters, e.g. ['MeanIntensity', 'Size']
        :return: a dictionary of data for each well e.g. {'A1': {'MeanIntensity': np.array(), 'Size': np.array()}}
        """
        if well_num is None:
            well_num = ['A1']
        if plot_param is None:
            plot_param = ['MeanIntensity']
        # Loop through each well in the ELISpot data
        data = {}
        for well in self.root.findall(f'.//{self.well_name}'):
            # Get the well's row and column number
            row = get_letter(int(well.find('./Row').text))
            col = int(well.find('./Column').text)
            if row + str(col) in well_num:
                spot_count = int(well.find('./WellResult/ActualSpotCount').text)
                #print(f'Well {row},{col}, {spot_count}')
                # Get the well's spot data
                spot_list = well.findall('./WellResult/Spot_List/Spot')
                # extract the data from each spot
                well = {param: np.array([]) for param in plot_param}
                for spot in spot_list:
                    for param in plot_param:
                        well[param] = np.append(well[param], [float(spot.find(f'./{param}').text)])
                data[row + str(col)] = well
        return data
