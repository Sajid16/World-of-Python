# Data Preprocessing Template

# Importing the libraries
'''import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""
'''

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