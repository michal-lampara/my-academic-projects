import pandas
import pydotplus
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
dtree = DecisionTreeClassifier(max_depth=4, random_state=0)
dtree = dtree.fit(X, y)

print("Accuracy on training set: {:.3f}".format(dtree.score(X, y)))
print("Accuracy on test set: {:.3f}".format(dtree.score(X, y)))

print("Feature importances:")
print(dtree.feature_importances_)