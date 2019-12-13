from pyTsetlinMachine.tm import MultiClassTsetlinMachine
import numpy as np
from time import time

# Parameters
# split_ratio = 0.9
epochs = 50
clauses = 4000
T = 8800
s = 27
k_fold_amount = 10

print("epochs = ", epochs)
print("clauses = ", clauses)
print("T = ", T)
print("s = ", s, "\n")

X_train = np.array([])
Y_train = np.array([])
X_test = np.array([])
Y_test = np.array([])

base_path_start = "Data/KfoldDataStaticTransformed/"
base_path_end = "statickfoldcorrected.data"
# path_train = "Data/eventrain.data"
# path_test = "Data/eventest.data"


def merging_k_fold(file_amount, _clauses, _T, _s, _epochs):
    results = []
    for i in range(file_amount):
        train_string = base_path_start + str(i) + "train" + base_path_end
        test_string = base_path_start + str(i) + "test" + base_path_end
        score = loading_data(train_string, test_string, _clauses, _T, _s, _epochs)
        results.append(score)

    return results


def loading_data(_train, _test, _clauses, _T, _s, _epochs):
    print("Loading training data..")
    train_data = np.loadtxt(_train, delimiter=",")
    # print("..using train dataset: ", _path_train)
    global X_train
    global Y_train
    X_train = train_data[:, 0:-1]
    Y_train = train_data[:, -1]

    print("Loading test data..")
    test_data = np.loadtxt(_test, delimiter=",")
    # print("..using test dataset: ", _path_test)
    global X_test
    global Y_test
    X_test = test_data[:, 0:-1]
    Y_test = test_data[:, -1]

    return TM(_clauses, _T, _s, epochs)


def TM(_clauses, _T, _s, _epochs):
    print("Creating MultiClass Tsetlin Machine.")
    tm = MultiClassTsetlinMachine(_clauses, _T, _s, boost_true_positive_feedback=0, weighted_clauses=True)
    print("Starting TM with weighted clauses..")
    print("\nAccuracy over ", _epochs, " epochs:\n")
    for i in range(_epochs):
        start = time()
        tm.fit(X_train, Y_train, epochs=1, incremental=True)
        stop = time()
        result = 100 * (tm.predict(X_test) == Y_test).mean()
        print("#%d Accuracy: %.2f%% (%.2fs)" % (i + 1, result, stop - start))

    mean_accuracy = 100 * (tm.predict(X_test) == Y_test).mean()
    print("Mean Accuracy:", mean_accuracy)
    print("Finished running.. \n")

    return mean_accuracy


score = merging_k_fold(k_fold_amount, clauses, T, s, epochs)
print(score)
