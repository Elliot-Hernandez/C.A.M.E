# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:44:54 2021

@author: Elliot
"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
x = pd.read_csv('C:/Users/Luis/Desktop/Elliot/Proyecto Terminal/freesound-python/C.A.M.E/PRUEBAAAA/D_STD_RMS.csv')
y = pd.read_csv('C:/Users/Luis/Desktop/Elliot/Proyecto Terminal/freesound-python/C.A.M.E/PRUEBAAAA/D_STD_ZCR.csv')
data = [x, y]
dc = pd.concat(data, axis=1)
kmeans = KMeans(n_clusters=7).fit(dc)
centroids = kmeans.cluster_centers_
print(centroids)
labels = kmeans.labels_
print(labels)
markers='s'
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



list_labels = list(labels)
list_labels.insert(0, 0)

--------------------------------------------------------
#Crear un CSV o XLS para una extracción mas rapida de los datos
from numpy import asarray
from numpy import savetxt

#text_labels = savetxt("list_labels_clusters.txt", list_labels, delimiter=',')
text_labels = savetxt("list_labels_clusters_csv.csv", list_labels, delimiter=',')


-------------------------------------------------------
#Sacar los indices de los sonidos basandose en la etiqueta del clúster
from xlrd import open_workbook

book = open_workbook('C:/Users/Luis/Desktop/list_labels_clusters_csv_PYTHON.xls')
list_cells_2 = []
for sheet in book.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
            if cell.value == 0 : #etiqueta del cluster
                list_cells_2.append(rowidx)
                #print(sheet.name)
                #print(colidx)
                #print(rowidx)



import pandas as pd

df = pd.DataFrame(list_cells_2)
df.to_csv ('dataframe.csv', index = False, header=False)
