# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: clustering.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 4/28/23 03:03
"""
from GroupAnalysis import GroupAnalysis
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, SpectralClustering, Birch, MeanShift
from sklearn.preprocessing import StandardScaler, MinMaxScaler

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

clp_il7_ifng = gp.one_group_aggregation('CLP+IL7-IFNg', ['Size', 'MeanIntensity'])
X = np.column_stack((clp_il7_ifng['Size'], clp_il7_ifng['MeanIntensity']))

# Create a list of clustering algorithms to test
clustering_algorithms = [
    KMeans(n_clusters=2),
    DBSCAN(eps=30, min_samples=20),
    #AgglomerativeClustering(n_clusters=2),
    #DBSCAN(eps=0.3, min_samples=5),
    #SpectralClustering(n_clusters=2),
    #Birch(n_clusters=2),
    #MeanShift()
]

scalers = [
    StandardScaler(),
    MinMaxScaler(),
]

# Fit each algorithm to the dataset and plot the results
fig, axs = plt.subplots(1+len(scalers), len(clustering_algorithms), figsize=(8*len(clustering_algorithms), 8*(1+len(scalers))))

for i, algorithm in enumerate(clustering_algorithms):
    algorithm.fit(X)
    labels = algorithm.labels_
    if len(clustering_algorithms) == 1:
        axs.scatter(X[:, 0], X[:, 1], c=labels, s=5)
        axs.set_title(type(algorithm).__name__)
        axs.set_xscale('log')
        axs.set_yscale('log')
    else:
        axs[i].scatter(X[:, 0], X[:, 1], c=labels, s=5)
        axs[i].set_title(type(algorithm).__name__)
        axs[i].set_xscale('log')
        axs[i].set_yscale('log')
plt.xlabel('MeanIntensity')
plt.ylabel('Size')
plt.show()
