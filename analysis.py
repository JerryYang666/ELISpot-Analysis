# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: analysis.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 4/28/23 01:39
"""
from GroupAnalysis import GroupAnalysis
from scipy.stats import f_oneway, skew
import numpy as np


def delete_outlier(data_ls):
    """
    delete outliers
    :param data_ls: a list of data
    :return: a list of data without outliers
    """
    new_ls = []
    for data1 in data_ls:
        data_mean = np.mean(data1)
        data_std = np.std(data1)
        data1 = data1[data1 < data_mean + 3 * data_std]
        data1 = data1[data1 > data_mean - 3 * data_std]
        new_ls.append(data1)
    return new_ls


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

# size

naive_ifng = gp.one_group_aggregation('Naive-IFNg', ['Size'])['Size']
clp_hemevehicle_ifng = gp.one_group_aggregation('CLP+HemeVehicle-IFNg', ['Size'])['Size']
clp_heme_ifng = gp.one_group_aggregation('CLP+Heme-IFNg', ['Size'])['Size']
clp_pbs_ifng = gp.one_group_aggregation('CLP+PBS-IFNg', ['Size'])['Size']
clp_il7_ifng = gp.one_group_aggregation('CLP+IL7-IFNg', ['Size'])['Size']

naive_tnfa = gp.one_group_aggregation('Naive-TNFa', ['Size'])['Size']
clp_hemevehicle_tnfa = gp.one_group_aggregation('CLP+HemeVehicle-TNFa', ['Size'])['Size']
clp_heme_tnfa = gp.one_group_aggregation('CLP+Heme-TNFa', ['Size'])['Size']
clp_pbs_tnfa = gp.one_group_aggregation('CLP+PBS-TNFa', ['Size'])['Size']
clp_il7_tnfa = gp.one_group_aggregation('CLP+IL7-TNFa', ['Size'])['Size']

print('Size-ifng', f_oneway(naive_ifng, clp_hemevehicle_ifng, clp_heme_ifng, clp_pbs_ifng, clp_il7_ifng))
print('Size-tnfa', f_oneway(naive_tnfa, clp_hemevehicle_tnfa, clp_heme_tnfa, clp_pbs_tnfa, clp_il7_tnfa))
print('')

# mean intensity
naive_ifng = gp.one_group_aggregation('Naive-IFNg', ['MeanIntensity'])['MeanIntensity']
clp_hemevehicle_ifng = gp.one_group_aggregation('CLP+HemeVehicle-IFNg', ['MeanIntensity'])['MeanIntensity']
clp_heme_ifng = gp.one_group_aggregation('CLP+Heme-IFNg', ['MeanIntensity'])['MeanIntensity']
clp_pbs_ifng = gp.one_group_aggregation('CLP+PBS-IFNg', ['MeanIntensity'])['MeanIntensity']
clp_il7_ifng = gp.one_group_aggregation('CLP+IL7-IFNg', ['MeanIntensity'])['MeanIntensity']


ifng_ls = delete_outlier([naive_ifng, clp_hemevehicle_ifng, clp_heme_ifng, clp_pbs_ifng, clp_il7_ifng])
ifng_group_name_ls = ['Naive-IFNg', 'CLP+HemeVehicle-IFNg', 'CLP+Heme-IFNg', 'CLP+PBS-IFNg', 'CLP+IL7-IFNg']

naive_tnfa = gp.one_group_aggregation('Naive-TNFa', ['MeanIntensity'])['MeanIntensity']
clp_hemevehicle_tnfa = gp.one_group_aggregation('CLP+HemeVehicle-TNFa', ['MeanIntensity'])['MeanIntensity']
clp_heme_tnfa = gp.one_group_aggregation('CLP+Heme-TNFa', ['MeanIntensity'])['MeanIntensity']
clp_pbs_tnfa = gp.one_group_aggregation('CLP+PBS-TNFa', ['MeanIntensity'])['MeanIntensity']
clp_il7_tnfa = gp.one_group_aggregation('CLP+IL7-TNFa', ['MeanIntensity'])['MeanIntensity']

tnfa_ls = delete_outlier([naive_tnfa, clp_hemevehicle_tnfa, clp_heme_tnfa, clp_pbs_tnfa, clp_il7_tnfa])
tnfa_group_name_ls = ['Naive-TNFa', 'CLP+HemeVehicle-TNFa', 'CLP+Heme-TNFa', 'CLP+PBS-TNFa', 'CLP+IL7-TNFa']

print('Mean Intensity-ifng', f_oneway(ifng_ls[0], ifng_ls[1], ifng_ls[2], ifng_ls[3], ifng_ls[4]))
for j, data in enumerate(ifng_ls):
    print(ifng_group_name_ls[j], ': Mean:', data.mean(), ' Std:', data.std())
print('')
print('Mean Intensity-tnfa', f_oneway(tnfa_ls[0], tnfa_ls[1], tnfa_ls[2], tnfa_ls[3], tnfa_ls[4]))
for j, data in enumerate(tnfa_ls):
    print(tnfa_group_name_ls[j], ': Mean:', data.mean(), ' Std:', data.std())
print('')

print('skewness')
for i, data in enumerate(ifng_ls):
    print(ifng_group_name_ls[i], ': ', skew(data))

for i, data in enumerate(tnfa_ls):
    print(tnfa_group_name_ls[i], ': ', skew(data))
