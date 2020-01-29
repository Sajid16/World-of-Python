import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
# X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 1.0, random_state = 0)

''' here splitting is not necessary because the dataset is very much small to split.
    so here we are going to use the whole dataset as train set and also as test set'''

# fitting linear regression model to the dataset
    
from sklearn.linear_model import LinearRegression
lin_regressor = LinearRegression()
model = lin_regressor.fit(X, y)
result_1 = lin_regressor.predict(X)
print('training accuracy score of linear regession: ', model.score(X, y))

# fitting polynomial regression to the dataset

from sklearn.preprocessing import PolynomialFeatures
ply_regression = PolynomialFeatures(degree = 2) # here degree value selects the power term. here it is (0-2)
X_poly = ply_regression.fit_transform(X)
lin_reg_2 = LinearRegression()
model_2 = lin_reg_2.fit(X_poly, y)
print('training accuracy score of polynomial regression: ', model_2.score(X_poly, y))


# visualizing the original value and predicted value with graph for linear regression

plt.scatter(X, y, color = 'red')
#plt.plot(X, lin_regressor.predict(X), color = 'blue')
plt.plot(X, result_1, color = 'blue')
plt.title('resulted graph for linear regression')
plt.xlabel('Level of jobs')
plt.ylabel('Salary')
plt.show()


# visualizing the original value and predicted value with graph for linear regression

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(X_poly), color = 'blue')
#plt.plot(X, result_1, color = 'blue')
plt.title('resulted graph for polynomial regression')
plt.xlabel('Level of jobs')
plt.ylabel('Salary')
plt.show()