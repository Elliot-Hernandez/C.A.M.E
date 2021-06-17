#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:24:38 2021

@author: elliot
"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np



x = pd.read_csv('/home/elliot/Documentos/Tésis/freesound-python/C.A.M.E/PRUEBAAAA/D_STD_RMS.csv')
y = pd.read_csv('/home/elliot/Documentos/Tésis/freesound-python/C.A.M.E/PRUEBAAAA/D_STD_ZCR.csv')
data = [x, y]
dc = pd.concat(data, axis=1)
kmeans = KMeans(n_clusters=2).fit(dc)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_


#labels = kmeans.predict(df)
#plt.scatter(x, y, c=labels.astype(float))
#plt.scatter(x, y, s=10, c=np.squeeze(y))

-----------------------------------------------------------------

#Elbow Metod

kmeans_kwargs = {
"init": "random",
"n_init": 10,
"max_iter": 300,
"random_state": 42,}

sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(dc)
    sse.append(kmeans.inertia_)

plt.style.use("fivethirtyeight")
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()


-----------------------------------------------------------------


def csv_clusters_2(path_x, path_y, n_clusters=2, markers='s'):
    x = pd.read_csv(path_x)
    y = pd.read_csv(path_y)

    data = [x, y]
    dc = pd.concat(data, axis=1)

    kmeans = KMeans(n_clusters).fit(dc)
    centroids = kmeans.cluster_centers_
    print(centroids)
    
    
    plt.scatter(x, y, s=50, c=labels.astype(float), marker='.')
    plt.scatter(centroids[0:, 0], centroids[0:, 1], s=200, c='g', marker=markers)
    plt.scatter(centroids[1:, 0], centroids[1:, 1], s=200, c='r', marker=markers)
    plt.scatter(centroids[2:, 0], centroids[2:, 1], s=200, c='gold', marker=markers)
    plt.scatter(centroids[3:, 0], centroids[3:, 1], s=200, c='cyan', marker=markers)
    plt.scatter(centroids[4:, 0], centroids[4:, 1], s=200, c='pink', marker=markers)
    plt.scatter(centroids[5:, 0], centroids[5:, 1], s=200, c='brown', marker=markers)
    plt.scatter(centroids[6:, 0], centroids[6:, 1], s=200, c='black', marker=markers)
    plt.scatter(centroids[7:, 0], centroids[7:, 1], s=200, c='orange', marker=markers)
    plt.scatter(centroids[8:, 0], centroids[8:, 1], s=200, c='yellow', marker=markers)
    plt.scatter(centroids[9:, 0], centroids[9:, 1], s=200, c='gray', marker=markers)
    plt.scatter(centroids[10:, 0], centroids[10:, 1], s=200, c='violet', marker=markers)
    plt.scatter(centroids[11:, 0], centroids[11:, 1], s=200, c='purple', marker=markers)
    plt.scatter(centroids[12:, 0], centroids[12:, 1], s=200, c='lime', marker=markers)
    plt.scatter(centroids[13:, 0], centroids[13:, 1], s=200, c='darkblue', marker=markers)
    plt.show()


-----------------------------------------------------------------


from mpl_toolkits.mplot3d import Axes3D

x = pd.read_csv()
y = pd.read_csv()
z = pd.read_csv()
data = [x, y, z]
dc = pd.concat(data, axis=1)#.fillna(0)

kmeans = KMeans(n_clusters=2).fit(dc)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(x, y, z, s=50, c=labels.astype(float), marker='.')
markers='s'
ax.scatter(centroids[0:, 0], centroids[0:, 1], s=200, c='g', marker=markers)
ax.scatter(centroids[1:, 0], centroids[1:, 1], s=200, c='r', marker=markers)
ax.scatter(centroids[2:, 0], centroids[2:, 1], s=200, c='gold', marker=markers)
ax.scatter(centroids[3:, 0], centroids[3:, 1], s=200, c='cyan', marker=markers)
ax.scatter(centroids[4:, 0], centroids[4:, 1], s=200, c='pink', marker=markers)
ax.scatter(centroids[5:, 0], centroids[5:, 1], s=200, c='brown', marker=markers)
ax.scatter(centroids[6:, 0], centroids[6:, 1], s=200, c='black', marker=markers)
ax.scatter(centroids[7:, 0], centroids[7:, 1], s=200, c='orange', marker=markers)
ax.scatter(centroids[8:, 0], centroids[8:, 1], s=200, c='yellow', marker=markers)
ax.scatter(centroids[9:, 0], centroids[9:, 1], s=200, c='gray', marker=markers)
ax.scatter(centroids[10:, 0], centroids[10:, 1], s=200, c='violet', marker=markers)
ax.scatter(centroids[11:, 0], centroids[11:, 1], s=200, c='purple', marker=markers)
ax.scatter(centroids[12:, 0], centroids[12:, 1], s=200, c='lime', marker=markers)
ax.scatter(centroids[13:, 0], centroids[13:, 1], s=200, c='darkblue', marker=markers)
plt.show()


ax.view_init(0,35)
fig

-----------------------------------------------------------------

"""
def csv_clusters(path_x, path_y, n_clusters=2, markers='s'):
    x = pd.read_csv(path_x)
    y = pd.read_csv(path_y)

    data = [x, y]
    dc = pd.concat(data, axis=1)

    kmeans = KMeans(n_clusters).fit(dc)
    centroids = kmeans.cluster_centers_
    print(centroids)
    
    plt.scatter(x, y, s =50, c='b', marker='.')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='g', marker=markers)
    plt.scatter(centroids[:, 2], centroids[:, 3], s=200, c='r', marker=markers)
    plt.scatter(centroids[:, 4], centroids[:, 5], s=200, c='gold', marker=markers)
    plt.scatter(centroids[:, 6], centroids[:, 7], s=200, c='cyan', marker=markers)
    plt.scatter(centroids[:, 8], centroids[:, 9], s=200, c='pink', marker=markers)
    plt.scatter(centroids[:, 10], centroids[:, 11], s=200, c='brown', marker=markers)
    plt.scatter(centroids[:, 12], centroids[:, 13], s=200, c='black', marker=markers)
    plt.scatter(centroids[:, 14], centroids[:, 15], s=200, c='orange', marker=markers)
    plt.scatter(centroids[:, 16], centroids[:, 17], s=200, c='yellow', marker=markers)
    plt.scatter(centroids[:, 18], centroids[:, 19], s=200, c='gray', marker=markers)
    plt.scatter(centroids[:, 20], centroids[:, 21], s=200, c='violet', marker=markers)
    plt.scatter(centroids[:, 22], centroids[:, 23], s=200, c='purple', marker=markers)
    plt.scatter(centroids[:, 24], centroids[:, 25], s=200, c='lime', marker=markers)
    plt.scatter(centroids[:, 26], centroids[:, 27], s=200, c='darkblue', marker=markers)
    plt.show()

"""




