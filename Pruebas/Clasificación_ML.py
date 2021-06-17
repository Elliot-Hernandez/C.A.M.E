#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:12:40 2021

@author: elliot
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

file = '/home/elliot/Documentos/Tésis/freesound-python/C.A.M.E/Archivos_CSV/Bass/ahj-subdrop-maxbass.wav.csv'

heart = pd.read_csv(file)

heart.head

heart.shape

heart['age'].unique()

feature_names = ['age','sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg','thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

X = heart[feature_names]

y = heart['num']

-------------------- estadistica ----------------------------------
heart['sex'].describe()
-------------------------------------------------------------------

-------------------- histograma -----------------------------------
plt.hist(heart['sex'], bins=16)
-------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

logreg = LogisticRegression()

logreg.fit(X_train, y_train)

logreg.score(X_train, y_train)

logreg.score(X_test, y_test)

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

knn.score(X_train, y_train)

knn.score(X_test, y_test)

-------------------------------------------------------

clf = DecisionTreeClassifier().fit(X_train, y_train)

clf.score(X_train, y_train)

clf.score(X_test, y_test)
