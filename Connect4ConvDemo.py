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
3. Look at clauses. Make a draw function that display what the clauses "learn".
4. Add 'Draw' to the dataset.
"""
# Parameters
epochs = 100
clauses = 10000
T = 80
s = 27

shape_x = 7
shape_y = 6
shape_z = 2

frame_x = 6
frame_y = 5

train_data = np.loadtxt("Data/trainingdata.txt", delimiter=",")
X_train = train_data[:, 0:-1].reshape(train_data.shape[0], shape_x, shape_y, shape_z)
Y_train = train_data[:, -1]

test_data = np.loadtxt("Data/testdata.txt", delimiter=",")
X_test = test_data[:, 0:-1].reshape(test_data.shape[0], shape_x, shape_y, shape_z)
Y_test = test_data[:, -1]

# Version 1:
"""
ctm = MultiClassConvolutionalTsetlinMachine2D(clauses, T, s, (frame_x, frame_y), boost_true_positive_feedback=0)
ctm.fit(X_train, Y_train, epochs=iterations)
print("Accuracy:", 100*(ctm.predict(X_test) == Y_test).mean())
"""
# Version 2:
tm = MultiClassConvolutionalTsetlinMachine2D(clauses, T, s, (frame_x, frame_y))
print("\nAccuracy over " + str(epochs) + " epochs:\n")
for i in range(epochs):
    start = time()
    tm.fit(X_train, Y_train, epochs=1, incremental=True)
    stop = time()
    result = 100 * (tm.predict(X_test) == Y_test).mean()
    print("#%d Accuracy: %.2f%% (%.2fs)" % (i + 1, result, stop - start))

print("Mean Accuracy:", 100*(tm.predict(X_test) == Y_test).mean())
