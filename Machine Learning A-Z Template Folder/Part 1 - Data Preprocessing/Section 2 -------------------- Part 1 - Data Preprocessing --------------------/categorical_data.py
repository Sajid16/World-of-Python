import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('D:\World-of-Python\Machine Learning A-Z Template Folder\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Data.csv')
dataset.head(10)

# X = dataset.iloc[2:8, :-1]
X = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, 3]
y = dataset.iloc[:, 3].values

# there is some mismatch between tutorial and this code in the package section. Imputer package doesn't support anyhow and i have used SimpleImputer in this case.

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
ip_mean = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
X[:, 0] = labelencoder_x.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)