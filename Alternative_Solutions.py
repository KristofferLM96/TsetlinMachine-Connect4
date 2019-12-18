from pyTsetlinMachine.tm import MultiClassTsetlinMachine
import numpy as np
from time import time
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


# Parameters
epochs = 50
clauses = 4000
T = 8800
s = 27
k_fold_amount = 10

X_train = np.array([])
Y_train = np.array([])
X_test = np.array([])
Y_test = np.array([])

base_path_start = "Data/KfoldDataStaticTransformed/"
base_path_end = "statickfoldcorrected.data"

results = []


def merging_k_fold(file_amount, _clauses, _T, _s, _epochs):
    results = []
    for i in range(file_amount):
        print("Running k-fold - ", i+1)
        train_string = base_path_start + str(i) + "train" + base_path_end
        test_string = base_path_start + str(i) + "test" + base_path_end
        score = loading_data(train_string, test_string, _clauses, _T, _s, _epochs)
        results.append(score)

    return results


def loading_data(_train, _test, _clauses, _T, _s, _epochs):
    train_data = np.loadtxt(_train, delimiter=",")
    global X_train
    global Y_train
    X_train = train_data[:, 0:-1]
    Y_train = train_data[:, -1]

    test_data = np.loadtxt(_test, delimiter=",")
    global X_test
    global Y_test
    X_test = test_data[:, 0:-1]
    Y_test = test_data[:, -1]

    return app(_epochs)


def app(_epochs):
    SVC_model = svm.SVC()
    """
    print("\nAccuracy over ", _epochs, " epochs:\n")
    for i in range(_epochs):
        start = time()
        SVC_model.fit(X_train, Y_train)
        stop = time()
        result = 100 * (SVC_model.predict(X_test) == Y_test).mean()
        print("#%d Accuracy: %.2f%% (%.2fs)" % (i + 1, result, stop - start))
    """
    SVC_model.fit(X_train, Y_train)
    result = 100 * (SVC_model.predict(X_test) == Y_test).mean()
    print("Accuracy:", result, "\n")
    global results
    results.append(result)

    """
    print("SVM: ")
    SVC_model = svm.SVC()
    SVC_model.fit(X_train, Y_train)
    SVC_prediction = SVC_model.predict(X_test)
    print(accuracy_score(SVC_prediction, Y_test)*100)
    print(classification_report(SVC_prediction, Y_test), "\n")

    print("Logistic Regression: ")
    logreg_clf = LogisticRegression()
    logreg_clf.fit(X_train, Y_train)
    logreg_prediction = logreg_clf.predict(X_test)
    print(accuracy_score(logreg_prediction, Y_test) * 100)
    print(classification_report(logreg_prediction, Y_test), "\n")

    print("Decision Tree Classifier: ")
    DTC_model = DecisionTreeClassifier()
    DTC_model.fit(X_train, Y_train)
    DTC_prediction = DTC_model.predict(X_test)
    print(accuracy_score(DTC_prediction, Y_test) * 100)
    print(classification_report(DTC_prediction, Y_test), "\n")

    print("Gaussian Naive_Bayes: ")
    G_NB = GaussianNB()
    G_NB.fit(X_train, Y_train)
    G_NB_prediction = G_NB.predict(X_test)
    print(accuracy_score(G_NB_prediction, Y_test) * 100)
    print(classification_report(G_NB_prediction, Y_test), "\n")

    print("Multinomial Naive_Bayes: ")
    M_NB = GaussianNB()
    M_NB.fit(X_train, Y_train)
    M_NB_prediction = M_NB.predict(X_test)
    print(accuracy_score(M_NB_prediction, Y_test) * 100)
    print(classification_report(M_NB_prediction, Y_test), "\n")

    print("BernoulliNB Naive_Bayes: ")
    B_NB = GaussianNB()
    B_NB.fit(X_train, Y_train)
    B_NB_prediction = B_NB.predict(X_test)
    print(accuracy_score(B_NB_prediction, Y_test) * 100)
    print(classification_report(B_NB_prediction, Y_test), "\n")

    print("Stochastic Gradient Descent: ")
    SGD = SGDClassifier()
    SGD.fit(X_train, Y_train)
    SGD_prediction = SGD.predict(X_test)
    print(accuracy_score(SGD_prediction, Y_test) * 100)
    print(classification_report(SGD_prediction, Y_test), "\n")
    """

    return result


score = merging_k_fold(k_fold_amount, clauses, T, s, epochs)
print(score)
result = 0
for i in range(len(results)):
    result = result + results[i]

result = result / k_fold_amount
print("Mean Accuracy for ", k_fold_amount, " k-folds: ", result, " %")
