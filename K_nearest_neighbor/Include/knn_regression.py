import pandas as pd
import math
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv("petrol_consumption.csv")
# print(dataset.head())
# print(dataset.shape)

X = dataset.iloc[:, 0:4]
y = dataset.iloc[:, 4]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# calculating the number of rows of X_train
total_rows = len(X_train.axes[0])
total_rows = math.sqrt(total_rows)
total_rows = round(total_rows)
print(total_rows)

for i in range(1, 36):
    regressor = KNeighborsRegressor(n_neighbors=i)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    training_accuracy = regressor.score(X_train, y_train)
    testing_accuracy = regressor.score(X_test, y_test)

    print("this is for ", i)
    print('training accuracy: ', training_accuracy)
    print('testing accuracy: ', testing_accuracy)
    print(y_test)
    print(y_pred)
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print('\n')
