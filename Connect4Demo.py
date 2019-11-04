from pyTsetlinMachine.tm import MultiClassTsetlinMachine
import numpy as np
from time import time

# Parameters
split_ratio = 0.9
epochs = 100
clauses = 10000  # 11502
T = 80  # 30
s = 27  # 58.98

print("epochs = ", epochs)
print("clauses = ", clauses)
print("T = ", T)
print("s = ", s, "\n")

print("Loading training data..")
train = np.loadtxt("Data/eventrain.data", delimiter=",")
print("Loading test data..")
test = np.loadtxt("Data/eventest.data", delimiter=",")
X_train = train[:, 0:-1]
X_test = test[:, 0:-1]
Y_train = train[:, -1]
Y_test = test[:, -1]


def TM(_clauses, _T, _s, _epochs):
	print("Creating MultiClass Tsetlin Machine.")
	tm = MultiClassTsetlinMachine(_clauses, _T, _s, boost_true_positive_feedback=0)
	print("Starting TM..")
	print("\nAccuracy over ", _epochs, " epochs:\n")
	for i in range(_epochs):
		start = time()
		tm.fit(X_train, Y_train, epochs=1, incremental=True)
		stop = time()
		result = 100*(tm.predict(X_test) == Y_test).mean()
		print("#%d Accuracy: %.2f%% (%.2fs)" % (i+1, result, stop-start))

	print("Mean Accuracy:", 100*(tm.predict(X_test) == Y_test).mean())
	print("Finished running..")
	print("Shutting down.")


ConvTM(clauses, T, s, epochs)
