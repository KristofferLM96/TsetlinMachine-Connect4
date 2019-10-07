from pyTsetlinMachine.tm import MultiClassConvolutionalTsetlinMachine2D
import numpy as np
from time import time

# Parameters
train_data = np.loadtxt("Data/trainingdata.txt", delimiter=",")
X_train = train_data[:, 0:-1]
Y_train = train_data[:, -1]

test_data = np.loadtxt("Data/testdata.txt", delimiter=",")
X_test = test_data[:, 0:-1]
Y_test = test_data[:, -1]

ctm = MultiClassConvolutionalTsetlinMachine2D(40, 60, 3.9, (5, 4), boost_true_positive_feedback=0)
ctm.fit(X_train, Y_train, epochs=5000)
print("Accuracy:", 100*(ctm.predict(X_test) == Y_test).mean())
Xi = np.array([[
                [0, 1, 1, 0],
                [1, 1, 0, 1],
                [1, 0, 1, 1],
                [0, 0, 0, 1]]])

print("\nInput Image:\n")
print(Xi)
print("\nPrediction: %d" % (ctm.predict(Xi)))

"""
tm = MultiClassConvolutionalTsetlinMachine2D(8000, 200, 10.0, (10, 10))
print("\nAccuracy over 25 epochs:\n")
for i in range(25):
    start = time()
    tm.fit(X_train, Y_train, epochs=1, incremental=True)
    stop = time()

    result = 100 * (tm.predict(X_test) == Y_test).mean()

    print("#%d Accuracy: %.2f%% (%.2fs)" % (i + 1, result, stop - start))
"""
