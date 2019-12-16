
from pyTsetlinMachine.tm import MultiClassTsetlinMachine
import numpy as np
import random




highscore = 0


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




def KDataHandler(inputrawdata,testnumber,var1,var2,var3,epochs,kdatahighscore):
    rawdata = inputrawdata.copy()
    testdata = rawdata[testnumber]

    del rawdata[testnumber]
    traindata = rawdata[0]
    del rawdata[0]
    
    
    while len(rawdata) > 0:
            traindata = np.concatenate((traindata, rawdata[0]))
            #traindata = list(traindata)
            del rawdata[0]
    
    random.shuffle(traindata)
    X_train = traindata[:, 0:-1]
    Y_train = traindata[:, -1]

    random.shuffle(testdata)
    X_test = testdata[:, 0:-1]
    Y_test = testdata[:, -1]
    
    return (smartTsetlin(var1,var2,var3,epochs,kdatahighscore,X_train,Y_train,X_test,Y_test))
    

    
def KFold(basepath,fileamount,var1,var2,var3,epochs,KFhighscore):
    rawfulldata = []
    for i in range(fileamount):
        fname = str(i) + basepath
        thisdata = np.loadtxt(fname, delimiter=",")
        rawfulldata.append(thisdata)

    results = []
    for i in range(fileamount):
        score, newhighscore = KDataHandler(rawfulldata,i,var1,var2,var3,epochs,KFhighscore)
        results.append(score)
        if newhighscore > KFhighscore:
            KFhighscore = newhighscore
            
    return results,KFhighscore




basepath = "verybigbindata.data"
score, highscore = KFold(basepath, 10, 500, 12, 27.3, 50, highscore)
print(score)





