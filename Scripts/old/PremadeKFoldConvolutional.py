from pyTsetlinMachine.tm import MultiClassConvolutionalTsetlinMachine2D
import numpy as np
import random
from time import time

highscore = 0

"""
def smartTsetlin(var1, var2, var3, somepochs, thishighscore, X_train, Y_train, X_test, Y_test):
    tm = MultiClassTsetlinMachine(var1, var2, var3, boost_true_positive_feedback=0)

    tm.fit(X_train, Y_train, epochs=somepochs)

    print(var1," ",var2," ",var3," ",somepochs)
    accuracy = 100*(tm.predict(X_test) == Y_test).mean()
    print("Accuracy:", " ", accuracy)

    #Save shit

    if(accuracy > thishighscore):

        thishighscore = 100*(tm.predict(X_test) == Y_test).mean()

        acstr = str(100*(tm.predict(X_test) == Y_test).mean())
        with open("KFoldMulticlassprint.txt", "a+") as myfile:
            myfile.write("var1: " + str(var1) + " var2: " + str(var2) + " var3: " + str(var3) + " epochs: " + str(somepochs) + " accuracy: " + acstr + "\n")
        myfile.close()

    return accuracy,thishighscore
"""


def Conv(var1, var2, var3, somepochs, thishighscore, X_train, Y_train, X_test, Y_test, frame_x, frame_y):
    print("Creating MultiClass Convolutional Tsetlin Machine.")
    tm = MultiClassConvolutionalTsetlinMachine2D(var1, var2, var3, (frame_x, frame_y))
    print("Starting ConvTM..")
    print("\nAccuracy over " + str(somepochs) + " epochs:\n")
    result = 0
    for i in range(somepochs):
        start = time()
        tm.fit(X_train, Y_train, epochs=1, incremental=True)
        stop = time()
        result = 100 * (tm.predict(X_test) == Y_test).mean()
        print("#%d Accuracy: %.2f%% (%.2fs)" % (i + 1, result, stop - start))

        # Save shit
    if (result > thishighscore):
        thishighscore = result

        acstr = str(result)
        with open("KFoldConvprint.txt", "a+") as myfile:
            myfile.write("var1: " + str(var1) + " var2: " + str(var2) + " var3: " + str(var3) + " epochs: " + str(
                somepochs) + " accuracy: " + acstr + "\n")
        myfile.close()
    return result, thishighscore


def KDataHandler(train, test, testnumber, var1, var2, var3, epochs, kdatahighscore, shape_x, shape_y, shape_z, frame_x,
                 frame_y):
    traindata = np.loadtxt(train, delimiter=",")
    X_train = traindata[:, 0:-1].reshape(traindata.shape[0], shape_x, shape_y, shape_z)
    Y_train = traindata[:, -1]

    testdata = np.loadtxt(test, delimiter=",")
    X_test = testdata[:, 0:-1].reshape(testdata.shape[0], shape_x, shape_y, shape_z)
    Y_test = testdata[:, -1]

    return (Conv(var1, var2, var3, epochs, kdatahighscore, X_train, Y_train, X_test, Y_test, frame_x, frame_y))


def KFold(basepath, fileamount, var1, var2, var3, epochs, KFhighscore, shape_x, shape_y, shape_z, frame_x, frame_y):
    results = []
    for i in range(fileamount):
        trainstring = str(i) + "train" + basepath
        teststring = str(i) + "test" + basepath
        score, newhighscore = KDataHandler(trainstring, teststring, i, var1, var2, var3, epochs, KFhighscore, shape_x,
                                           shape_y, shape_z, frame_x, frame_y)
        results.append(score)
        if newhighscore > KFhighscore:
            KFhighscore = newhighscore

    return results, KFhighscore


basepath = "statickfold.data"
score, highscore = KFold(basepath, 10, 11502, 51, 39.27, 500, highscore, 7, 6, 2, 6, 5)
print(score)


