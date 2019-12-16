# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#importing dataset and splitting into train and test set
dataset = pd.read_csv('Salary_Data.csv')
dataset.head(10)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.25, random_state = 0)

# feature scaling
#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)

# implementing linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
model = regressor.fit(X_train, y_train)
print('training score: ',model.score(X_train, y_train))


# Predicting the Test set results
y_pred = model.predict(X_test)
print('testing score: ',model.score(X_test, y_test))

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, model.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
# plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.plot(X_test, y_pred, color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

print('Another testing is starting from here')
test_dataset = pd.read_csv('Salary_Data_Test.csv')
test_dataset.head(5)

y_test_pred = model.predict(test_dataset)
print('Pure_testing score: ',model.score(test_dataset, y_test_pred))
# Visualising the Test set results
plt.scatter(test_dataset, y_test_pred, color = 'red')
plt.plot(X_train, model.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# np.savetxt('Salary_Data_Test.csv', y_test_pred, fmt='%d' , header='Salary')