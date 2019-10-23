import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
# X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 1.0, random_state = 0)

''' here splitting is not necessary because thae dataset is very much small to split.
    so here we are going to use the whole dataset as train set and also as test set'''

# fitting linear regression model to the dataset
    
from sklearn.linear_model import LinearRegression
lin_regressor = LinearRegression()
model = lin_regressor.fit(X, y)
print('training accuracy score: ', model.score(X, y))

# fitting polynomial regression to the dataset

from sklearn.preprocessing import PolynomialFeatures
ply_regression = PolynomialFeatures(degree = 2) # here degree value selects the power term. here it is (0-2)
X_poly = ply_regression.fit_transform(X)