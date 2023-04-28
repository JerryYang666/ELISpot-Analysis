# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: test.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 4/27/23 22:04
"""

from GetDataFromXML import GetDataFromXML

xml_path = 'data/042221_CLP_IL7_heme_for_nanostring.xml'
well_name = 'QCWell'
plot_param = ['MeanIntensity', 'Size']
well_num = ['A1', 'A2']

data = GetDataFromXML(xml_path, well_name).get_data(well_num, plot_param)
print(data)

