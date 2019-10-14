from pyTsetlinMachine.tm import MultiClassConvolutionalTsetlinMachine2D
import numpy as np
from time import time

# ****************************************************
# ******************** TO-DO *************************
# ****************************************************
"""
1. Create "proper" code for creating/splitting/shuffling of the dataset.
2. Test with different parameters for the ConvTM.
2.1. Different sizes of the window/frame
2.2. Possibly add more epochs. Seems to still increase after 50.
3. Add 'Draw' to the dataset.
4. Look at clauses. Make a draw function that display what the clauses "learn".

"""
# Parameters
iterations = 50
shape_x = 7
shape_y = 6
shape_z = 2
frame_x = 5
frame_y = 4
clauses = 10000
T = 80
s = 27

train_data = np.loadtxt("Data/trainingdata.txt", delimiter=",")
X_train = train_data[:, 0:-1].reshape(train_data.shape[0], shape_x, shape_y, shape_z)
Y_train = train_data[:, -1]

# shape[0] Should be the length of the amount of examples.
print(X_train.shape[0])
# shape[1] Should be the length of the x-coordinates.
print(X_train.shape[1])
# shape[2] Should be the length of the y-coordinates.
print(X_train.shape[2])
# shape[3] Should be the length of the y-coordinates.
print(X_train.shape[3])


test_data = np.loadtxt("Data/testdata.txt", delimiter=",")
X_test = test_data[:, 0:-1]
Y_test = test_data[:, -1]

# Version 1:
"""
ctm = MultiClassConvolutionalTsetlinMachine2D(clauses, T, s, (frame_x, frame_y), boost_true_positive_feedback=0)
ctm.fit(X_train, Y_train, epochs=iterations)
print("Accuracy:", 100*(ctm.predict(X_test) == Y_test).mean())
"""
# Version 2:
tm = MultiClassConvolutionalTsetlinMachine2D(clauses, T, s, (frame_x, frame_y))
print("\nAccuracy over " + str(iterations) + " epochs:\n")
for i in range(iterations):
    start = time()
    tm.fit(X_train, Y_train, epochs=1, incremental=True)
    stop = time()
    result = 100 * (tm.predict(X_test) == Y_test).mean()
    print("#%d Accuracy: %.2f%% (%.2fs)" % (i + 1, result, stop - start))

print("Mean Accuracy:", 100*(tm.predict(X_test) == Y_test).mean())
