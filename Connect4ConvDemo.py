from pyTsetlinMachine.tm import MultiClassConvolutionalTsetlinMachine2D
import numpy as np
from time import time

# Parameters
epochs = 100
clauses = 10000  # 11502
T = 90  # 30
s = 27  # 58.98

shape_x = 7
shape_y = 6
shape_z = 2

frame_x = 6
frame_y = 5

print("epochs = ", epochs)
print("clauses = ", clauses)
print("T = ", T)
print("s = ", s, "\n")
print("shape_x = ", shape_x)
print("shape_y = ", shape_y)
print("shape_z = ", shape_z, "\n")
print("frame_x = ", frame_x)
print("frame_y = ", frame_y, "\n")

print("Loading training data..")
train_data = np.loadtxt("Data/eventrain.data", delimiter=",")
X_train = train_data[:, 0:-1].reshape(train_data.shape[0], shape_x, shape_y, shape_z)
Y_train = train_data[:, -1]

print("Loading test data..")
test_data = np.loadtxt("Data/eventest.data", delimiter=",")
X_test = test_data[:, 0:-1].reshape(test_data.shape[0], shape_x, shape_y, shape_z)
Y_test = test_data[:, -1]


def ConvTM(_clauses, _T, _s, _epochs, _frame_x, _frame_y):
    print("Creating MultiClass Convolutional Tsetlin Machine.")
    tm = MultiClassConvolutionalTsetlinMachine2D(_clauses, _T, _s, (_frame_x, _frame_y))
    print("Starting ConvTM..")
    print("\nAccuracy over " + str(_epochs) + " epochs:\n")
    for i in range(_epochs):
        start = time()
        tm.fit(X_train, Y_train, epochs=1, incremental=True)
        stop = time()
        result = 100 * (tm.predict(X_test) == Y_test).mean()
        print("#%d Accuracy: %.2f%% (%.2fs)" % (i + 1, result, stop - start))

    print("Mean Accuracy:", 100*(tm.predict(X_test) == Y_test).mean(), "\n")
    print("Finished running..")
    print("Shutting down.")


ConvTM(clauses, T, s, epochs, frame_x, frame_y)
