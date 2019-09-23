from pyTsetlinMachine.tm import MultiClassTsetlinMachine
import numpy as np

# Parameters
split_ratio = 0.9
train_data = np.loadtxt("Data/bitcode-connect-4.data", delimiter=",")

X = train_data[:, 0:-1]
Y = train_data[:, -1]

X_train = X[:int(len(X) * split_ratio)]
X_test = X[int(len(X) * split_ratio):]

Y_train = Y[:int(len(Y) * split_ratio)]
Y_test = Y[int(len(Y) * split_ratio):]

tm = MultiClassTsetlinMachine(1000, 15, 3.9, boost_true_positive_feedback=0)

tm.fit(X_train, Y_train, epochs=200)

print("Accuracy:", 100*(tm.predict(X_test) == Y_test).mean())

print("Prediction: x1 = 1, x2 = 0, ... -> y = %d" % (tm.predict(np.array([[1,0,1,0,1,0,1,1,1,1,0,0]]))))
print("Prediction: x1 = 0, x2 = 1, ... -> y = %d" % (tm.predict(np.array([[0,1,1,0,1,0,1,1,1,1,0,0]]))))
print("Prediction: x1 = 0, x2 = 0, ... -> y = %d" % (tm.predict(np.array([[0,0,1,0,1,0,1,1,1,1,0,0]]))))
print("Prediction: x1 = 1, x2 = 1, ... -> y = %d" % (tm.predict(np.array([[1,1,1,0,1,0,1,1,1,1,0,0]]))))
