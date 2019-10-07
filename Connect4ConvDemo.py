from pyTsetlinMachine.tm import MultiClassConvolutionalTsetlinMachine2D
import numpy as np
from time import time

"""
Player-X:  0-41  (42)
Player-O: 42-83  (42)

Player-X: 42 plasser (7x6)
Player: 42 plasser (7x6)

Have to get ConvTM to understand that it is working with a 7x6 image times 2.
That means that it is a 7x6 image for player-X and 7x6 image for player-O.
"""

# Parameters
train_data = np.loadtxt("Data/trainingdata.txt", delimiter=",")
X_train = train_data[:, 0:-1]#.reshape[train_data.shape[0], 7, 6]
Y_train = train_data[:, -1]

# shape[0] Should be the length of the amount of examples.
print(X_train.shape[0])
# shape[1] Should be the length of the x-coordinates.
print(X_train.shape[1])
# shape[2] Should be the length of the y-coordinates.
print(X_train.shape[2])

test_data = np.loadtxt("Data/testdata.txt", delimiter=",")
X_test = test_data[:, 0:-1]
Y_test = test_data[:, -1]

# Version 1:
"""
ctm = MultiClassConvolutionalTsetlinMachine2D(40, 7, 6, (5, 4), boost_true_positive_feedback=0)
ctm.fit(X_train, Y_train, epochs=5000)
print("Accuracy:", 100*(ctm.predict(X_test) == Y_test).mean())
"""
# Version 2:
"""
tm = MultiClassConvolutionalTsetlinMachine2D(8000, 200, 10.0, (5, 4))
print("\nAccuracy over 25 epochs:\n")
for i in range(25):
    start = time()
    tm.fit(X_train, Y_train, epochs=1, incremental=True)
    stop = time()
    result = 100 * (tm.predict(X_test) == Y_test).mean()
    print("#%d Accuracy: %.2f%% (%.2fs)" % (i + 1, result, stop - start))
"""
