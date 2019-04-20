#importing libraries

import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('dataset.csv')
#printing dataset size on the basis of row and column
#print(dataset.shape)

#printing some top dataset values
#print(dataset.head(10))

#initializing inputs and outputs
X = dataset['Head Size(cm^3)'].values
Y = dataset['Brain Weight(grams)'].values

# print(len(X))
# print('\n')
# print(len(Y))

#finding mean of input and output
x_mean = np.mean(X)
y_mean = np.mean(Y)

# print(x_mean)
# print('\n')
# print(y_mean)

#total number of values
n = len(X)

numerator = 0
denominator = 0
for i in range(n):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2
b1 = numerator / denominator
b0 = y_mean - (b1 * x_mean)

# Print coefficients
#print(b1, b0)

# Plotting Values and Regression Line

max_x = np.max(X) + 100
min_x = np.min(X) - 100

# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

# Ploting Line
plt.plot(x, y, color='blue', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

# Calculating Root Mean Squares Error
rmse = 0
for i in range(n):
    y_pred = b0 + b1 * X[i]
    rmse += (Y[i] - y_pred) ** 2
rmse = np.sqrt(rmse/n)
print(rmse)

# Calculating R^2 Error
ss_t = 0
ss_r = 0
for i in range(n):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - y_mean) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = (1 - (ss_r/ss_t))*100
print(r2)