#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# encoding the string column
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
X[:, 3] = labelencoder_x.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# avoiding the dummy variable trap
X = X[:, 1:]

# splitting into train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# fitting multiple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("Training accuracy score: ", regressor.score(X_train, y_train))

# predicting the profit here
y_pred  = regressor.predict(X_test)
print("Testing accuracy score: ", regressor.score(X_test, y_test))

# training set plotting on graph
#plt.scatter(X_train[:,4], y_train, color = 'red')
#plt.plot(X_train[:,4], regressor.predict(X_train[:,4]), color = 'blue')
#plt.show()
    