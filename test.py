# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: test.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 4/27/23 22:04
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Generate some 3-dimensional data
data = np.random.rand(100, 3)

# Perform K-means clustering with 5 clusters
kmeans = KMeans(n_clusters=5)
labels = kmeans.fit_predict(data)

# Create a 3D scatter plot of the data, colored by cluster label
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,0], data[:,1], data[:,2], c=labels)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

