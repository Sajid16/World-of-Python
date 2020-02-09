# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:32:26 2020

@author: user
"""

# importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing dataset

dataset = pd.read_csv("bill_authentication.csv")
dataset.shape
dataset.head()

# X1 = dataset.iloc[:, :-1]
# y1 = dataset.iloc[:, -1]

X = dataset.drop('Class', axis=1)
y = dataset['Class']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
model = classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred, y_test))

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))