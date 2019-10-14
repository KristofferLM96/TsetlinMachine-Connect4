from pyTsetlinMachine.tm import MultiClassTsetlinMachine
import numpy as np
from time import time

# Parameters
split_ratio = 0.9
#train_data = np.loadtxt("Data/bitcode-connect-4.data", delimiter=",")

#X = train_data[:, 0:-1]
#Y = train_data[:, -1]

#X_train = X[:int(len(X) * split_ratio)]
#X_test = X[int(len(X) * split_ratio):]

#Y_train = Y[:int(len(Y) * split_ratio)]
#Y_test = Y[int(len(Y) * split_ratio):]

"""
Audun sitt dataset.
"""
# *********************************************************************************** #
train = np.loadtxt("Data/trainingdata.txt", delimiter=",")
test = np.loadtxt("Data/testdata.txt", delimiter=",")
X_train = train[:, 0:-1]
X_test = test[:, 0:-1]
Y_train = train[:, -1]
Y_test = test[:, -1]
# *********************************************************************************** #

tm = MultiClassTsetlinMachine(10000, 80, 27, boost_true_positive_feedback=0)

print("\nAccuracy over 50 epochs:\n")
for i in range(50):
	start = time()
	tm.fit(X_train, Y_train, epochs=1, incremental=True)
	stop = time()
	result = 100*(tm.predict(X_test) == Y_test).mean()
	print("#%d Accuracy: %.2f%% (%.2fs)" % (i+1, result, stop-start))

print("Mean Accuracy:", 100*(tm.predict(X_test) == Y_test).mean())