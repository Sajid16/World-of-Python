import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

dataset = pd.read_csv("bill_authentication.csv")
print(dataset.head())

X = dataset.iloc[:, 0:4]
y = dataset.iloc[:, 4]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

for i in range(1, 5):
    classifier = RandomForestClassifier(n_estimators=i, random_state=0)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    # print(accuracy_score(y_true, y_pred.round(), normalize=False))
    print(accuracy_score(y_test, y_pred))
