import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


# Parameters
epochs = 50
k_fold_amount = 10

X_train = np.array([])
Y_train = np.array([])
X_test = np.array([])
Y_test = np.array([])

base_path_start = "Data/KfoldDataStaticTransformed/"
base_path_end = "statickfoldcorrected.data"

acc_results = []


def merging_k_fold(file_amount, _epochs):
    results = []
    for i in range(file_amount):
        print("Running k-fold - ", i+1)
        train_string = base_path_start + str(i) + "train" + base_path_end
        test_string = base_path_start + str(i) + "test" + base_path_end
        score = loading_data(train_string, test_string, _epochs)
        results.append(score)

    return results


def loading_data(_train, _test, _epochs):
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

    return bnb(_epochs)


def svm(_epochs):
    # Support Vector Machines
    SVC_model = svm.SVC()
    SVC_model.fit(X_train, Y_train)
    acc_result = 100 * (SVC_model.predict(X_test) == Y_test).mean()
    print("Accuracy:", acc_result, "\n")
    global acc_results
    acc_results.append(acc_result)

    return acc_result


def log_reg(_epochs):
    # Logistic Regression
    logreg_clf = LogisticRegression()
    logreg_clf.fit(X_train, Y_train)
    acc_result = 100 * (logreg_clf.predict(X_test) == Y_test).mean()
    print("Accuracy:", acc_result, "\n")
    global acc_results
    acc_results.append(acc_result)

    return acc_result


def dtc(_epochs):
    # Decision Tree Classifier
    DTC_model = DecisionTreeClassifier()
    DTC_model.fit(X_train, Y_train)
    acc_result = 100 * (DTC_model.predict(X_test) == Y_test).mean()
    print("Accuracy:", acc_result, "\n")
    global acc_results
    acc_results.append(acc_result)

    return acc_result


def sgd(_epochs):
    # Stochastic Gradient Descent
    SGD = SGDClassifier()
    SGD.fit(X_train, Y_train)
    acc_result = 100 * (SGD.predict(X_test) == Y_test).mean()
    print("Accuracy:", acc_result, "\n")
    global acc_results
    acc_results.append(acc_result)

    return acc_result


def gnb(_epochs):
    # Naive Bayes Gaussian
    G_NB = GaussianNB()
    G_NB.fit(X_train, Y_train)
    acc_result = 100 * (G_NB.predict(X_test) == Y_test).mean()
    print("Accuracy:", acc_result, "\n")
    global acc_results
    acc_results.append(acc_result)

    return acc_result


def mnb(_epochs):
    # Naive Bayes Multinomial
    M_NB = MultinomialNB()
    M_NB.fit(X_train, Y_train)
    acc_result = 100 * (M_NB.predict(X_test) == Y_test).mean()
    print("Accuracy:", acc_result, "\n")
    global acc_results
    acc_results.append(acc_result)

    return acc_result


def bnb(_epochs):
    # Naive Bayes Bernoulli
    B_NB = BernoulliNB()
    B_NB.fit(X_train, Y_train)
    acc_result = 100 * (B_NB.predict(X_test) == Y_test).mean()
    print("Accuracy:", acc_result, "\n")
    global acc_results
    acc_results.append(acc_result)

    return acc_result


score = merging_k_fold(k_fold_amount, epochs)
print(score)
avg_result = 0
for i in range(len(acc_results)):
    avg_result = avg_result + acc_results[i]

avg_result = avg_result / k_fold_amount
print("Mean Accuracy for ", k_fold_amount, " k-folds: ", avg_result, " %")
