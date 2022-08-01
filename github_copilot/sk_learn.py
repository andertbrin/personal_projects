import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


# load the iris dataset
iris = load_iris()

# print the iris first four lines
print(iris.data[:4])

# split the dataset into training and test sets
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(iris.data, iris.target, test_size=0.3, random_state=0)

# train a model on the iris data
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# make predictions on the test set
y_pred = model.predict(X_test)

# print the accuracy of the model
print(sklearn.metrics.accuracy_score(y_test, y_pred))