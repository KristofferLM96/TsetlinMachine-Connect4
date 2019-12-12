from pyTsetlinMachine.tm import MultiClassTsetlinMachine
import numpy as np
import random

highscore = 0


def smartTsetlin(var1, var2, var3, somepochs, thishighscore, X_train, Y_train, X_test, Y_test):
    tm = MultiClassTsetlinMachine(var1, var2, var3, boost_true_positive_feedback=0)

    tm.fit(X_train, Y_train, epochs=somepochs)

    print(var1, " ", var2, " ", var3, " ", somepochs)
    accuracy = 100 * (tm.predict(X_test) == Y_test).mean()
    print("Accuracy:", " ", accuracy)

    # Save shit

    if (accuracy > thishighscore):
        thishighscore = accuracy

        acstr = str(accuracy)
        with open("KFoldMulticlassprint.txt", "a+") as myfile:
            myfile.write("var1: " + str(var1) + " var2: " + str(var2) + " var3: " + str(var3) + " epochs: " + str(
                somepochs) + " accuracy: " + acstr + "\n")
        myfile.close()

    return accuracy, thishighscore


def KDataHandler(train, test, testnumber, var1, var2, var3, epochs, kdatahighscore):
    traindata = np.loadtxt(train, delimiter=",")
    X_train = traindata[:, 0:-1]
    Y_train = traindata[:, -1]

    testdata = np.loadtxt(test, delimiter=",")
    X_test = testdata[:, 0:-1]
    Y_test = testdata[:, -1]

    return (smartTsetlin(var1, var2, var3, epochs, kdatahighscore, X_train, Y_train, X_test, Y_test))


def KFold(basepath, fileamount, var1, var2, var3, epochs, KFhighscore):
    results = []
    for i in range(fileamount):
        trainstring = "../Data/" + str(i) + "train" + basepath
        teststring = "../Data/" + str(i) + "test" + basepath
        score, newhighscore = KDataHandler(trainstring, teststring, i, var1, var2, var3, epochs, KFhighscore)
        results.append(score)
        if newhighscore > KFhighscore:
            KFhighscore = newhighscore

    return results, KFhighscore


basepath = "statickfold.data"

score, highscore = KFold(basepath, 10, 100, 51, 39.27, 50, highscore)
print(score)

score, highscore = KFold(basepath, 10, 1000, 51, 39.27, 50, highscore)
print(score)

score, highscore = KFold(basepath, 10, 11502, 51, 39.27, 50, highscore)
print(score)

score, highscore = KFold(basepath, 10, 100000, 51, 39.27, 50, highscore)
print(score)


