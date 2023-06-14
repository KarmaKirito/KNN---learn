import sklearn
from sklearn import datasets
import pickle
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_digits()
x = cancer.data
y = cancer.target
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

best = 0
'''run = True
while run:
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)
    clf = KNeighborsClassifier(n_neighbors=7)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    acc = metrics.accuracy_score(y_test, y_pred)
    print(best)
    if acc >= 1.0:
        with open('digits.pickle', 'wb') as f:
            pickle.dump(clf, f)
        run = False
    if acc > best:
        best = acc'''
pickle_in = open('digits.pickle', 'rb')
clf = pickle.load(pickle_in)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
acc = metrics.accuracy_score(y_test, y_pred)
print(acc)
