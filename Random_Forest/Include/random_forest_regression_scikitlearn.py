# import libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn import metrics

# import dataset

dataset = pd.read_csv("petrol_consumption.csv")
print(dataset.head())

# prepare data for training
# allocating feature columns into X and result column into y

X = dataset.iloc[:, 0:4]
y = dataset.iloc[:, 4]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# print('before\n')
# print(X_train)
print('after\n')
print(X_test)
# print('before y\n')
# print(y_train)
# print('after y\n')
# print(y_test)

# feature scaling

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# training the algorithm

regresseor = RandomForestRegressor(n_estimators=20, random_state=0)
regresseor.fit(X_train, y_train)
y_pred = regresseor.predict(X_test)
# accuracy = accuracy_score(y_pred, y_test)
print(y_pred)
