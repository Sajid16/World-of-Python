#KNN - predict whether a person have diabetes or not

# importing important libraries
import numpy as np
import pandas as pd
import math

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('diabetes.csv')
# print(len(dataset))
# print(dataset.head(10))

# replacing zero values of the important columns
zero_not_accepted = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']

i = 0
for column in zero_not_accepted:
    # t = dataset[column]
    # if t == '0':
    #     print(i+2)
    dataset[column] = dataset[column].replace(0, np.NaN)
    mean = int(dataset[column].mean(skipna=True))
    print(mean)
    dataset[column] = dataset[column].replace(np.NaN, mean)
print(dataset['Glucose'])

#splitting dataset
X = dataset.iloc[:, 0:8]
y = dataset.iloc[:, 8]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)

#feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

#define the model: init K-NN
classifier = KNeighborsClassifier(n_neighbors=11, p=2, metric='euclidean')

print(math.sqrt(len(y)))

#fit model
classifier.fit(X_train, y_train)

#predict the test set result
y_pred = classifier.predict(X_test)
print(y_pred)