from pandas import read_csv
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ["sepal length", "sepal width", "petal length", "petal width", "class"]
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:4]
Y = array[:,4]

# visualize data
# hist = dataframe.hist()
# plot = dataframe.plot(kind='box')
# scatter_matrix(dataframe)
# plt.show()


# prepare models
# models = []
# models.append(('LR', LogisticRegression()))
# models.append(('LDA', LinearDiscriminantAnalysis()))
# models.append(('SVC', SVC()))

# evaluate each model in turn
# results = []
# names = []
# scoring = 'accuracy'
# for name, model in models:
#     kfold = KFold(n_splits=10, random_state=7)
#     cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
#     results.append(cv_results)
#     names.append(name)
#     msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#     print(msg)

# split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
print('There are {} samples in the training set and {} samples in the test set'.format(X_train.shape[0], X_test.shape[0]))

# Applying SVM
svm = SVC(kernel='rbf', random_state=0, gamma=.10, C=1.0)
svm.fit(X_train, Y_train)
print('The accuracy of the SVM classifier on test data is {:.2f}'.format(svm.score(X_test, Y_test)))

# Applying Knn
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 7, p = 2, metric='minkowski')
knn.fit(X_train, Y_train)

print('The accuracy of the Knn classifier on test data is {:.2f}'.format(knn.score(X_test, Y_test)))

# Applying Decision Tree
from sklearn import tree

# Create tree object
decision_tree = tree.DecisionTreeClassifier(criterion='gini')

# Train DT based on scaled training set
decision_tree.fit(X_train, Y_train)

# Print performance
# print('The accuracy of the Decision Tree classifier on training data is {:.2f}'.format(decision_tree.score(X_train, Y_train)))
print('The accuracy of the Decision Tree classifier on test data is {:.2f}'.format(decision_tree.score(X_test, Y_test)))
print('Predict: ')
pred = decision_tree.predict([[12.7,12.8,8.1,8.3]])
for m in pred:
    print(m)


# Applying RandomForest
from sklearn.ensemble import RandomForestClassifier

# Create Random Forest object
random_forest = RandomForestClassifier()

# Train model
random_forest.fit(X_train, Y_train)

# Print performance
print('The accuracy of the Random Forest classifier on test data is {:.2f}'.format(random_forest.score(X_test, Y_test)))