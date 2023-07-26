import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['pregnant', 'glucose', 'bp', 'shin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv("pima-indians-diabetes.csv", header=None, names=col_names)
print(pima.head())
print(pima.sample(5))
print((pima.tail()))

feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']

X = pima[feature_cols]  # Feature
Y = pima.label  # target variable

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)  # 70% training and 30% testing
# crete decision tree classifier object
clf = DecisionTreeClassifier()
# train decision tree classifier
clf = clf.fit(X_train, Y_train)
# predict the response for the test dataset
Y_pred = clf.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))
