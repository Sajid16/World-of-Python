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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# print('before\n')
# print(X_train)
# print('after\n')
# print(X_test)
# print('before y\n')
# print(y_train)
# print('after y\n')
# print(y_test)

# feature scaling

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# print(X_train)

# training the algorithm

for i in range(1, 200):
    # print(i)
    regresseor = RandomForestRegressor(n_estimators=i, random_state=0)
    regresseor.fit(X_train, y_train)
    training_accuracy = regresseor.score(X_train, y_train)
    y_pred = regresseor.predict(X_test)
    testing_accuracy = regresseor.score(X_test, y_test)
    # print(y_pred)

    # evaluating the algorithm
    print("this is for ", i)
    print('training accuracy: ', training_accuracy)
    print('testing accuracy: ', testing_accuracy)
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print('\n')
