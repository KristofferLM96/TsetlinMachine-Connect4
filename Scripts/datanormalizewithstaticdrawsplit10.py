import math
import random

""" This script splits a binary data file into a train and 
test datafile which are almost evenly distributed in terms of wins and losses """

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

datasplits = 10
#trnd = open('xeventrain.data', 'w')
#tstd = open('xeventest.data', 'w')
"""Filepath refers to data file in binary form"""
filepath = "fullbindata.data"
with open(filepath) as fp:
    line = fp.readline()
    wins = []
    losses = []
    draws = []
    while line:
        binary = []
        #print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()

        if len(line) != 170:
            print("skip")
        elif line[-2] == "0":
            #losses.append(line)
            thislist = []
            for i in range(len(line)):
                if line[i] == '0':
                    thislist.append(0)
                elif line[i] == '1':
                    thislist.append(1)
            losses.append(thislist)
        elif line[-2] == "1":
            #losses.append(line)
            thislist = []
            for i in range(len(line)):
                if line[i] == '0':
                    thislist.append(0)
                elif line[i] == '1':
                    thislist.append(1)
            wins.append(thislist)
        elif line[-2] == "2":
            #losses.append(line)
            thislist = []
            for i in range(len(line)):
                if line[i] == '0':
                    thislist.append(0)
                elif line[i] == '1':
                    thislist.append(1)
                elif line[i] == '2':
                    thislist.append(2)
            draws.append(thislist)
        else:
            print("Not win nor loss nor draw")

    #print("Wins ", wins)
    #print("Losses ", losses)
    print("Amount of wins: ", len(wins))
    print("Amount of losses: ", len(losses))
    print("Amount of draws: ", len(draws))

    #Datainfo stores information about the split of wins,losses and draws accross all datasets
    datainfo = []
    for y in range(datasplits):
        thisinfo = []
        for o in range(3):
            thisinfo.append(0)
        datainfo.append(thisinfo)

    traintestdatas = []
    for g in range(datasplits):
        somelist = []
        traintestdatas.append(somelist)
    splitwin = round_down(len(wins)*(datasplits/100))
    splitloss = round_down(len(losses)*(datasplits/100))
    splitdraw = round_down(len(draws)*(datasplits/100))
    #ratio = round_down(len(wins)/len(losses))
    #testwin = len(wins) - trainwin
    #testloss = len(losses) - trainloss

    #Add win data
    changer = 0
    while True:
        if len(wins) <= 0:
            break
        if changer > datasplits-1:
            changer = 0
        else:
            traintestdatas[changer].append(wins[0])
            del wins[0]
            datainfo[changer][0] += 1
            changer += 1

    #Add loss data
    changer = 0
    while True:
        if len(losses) <= 0:
            break
        if changer > datasplits-1:
            changer = 0
        else:
            traintestdatas[changer].append(losses[0])
            del losses[0]
            datainfo[changer][1] += 1
            changer += 1

    #Add draw data
    changer = 0
    while True:
        if len(draws) <= 0:
            break
        if changer > datasplits-1:
            changer = 0
        else:
            traintestdatas[changer].append(draws[0])
            del draws[0]
            datainfo[changer][2] += 1
            changer += 1

    #Shuffle each dataset individually
    for v in range(datasplits):
        random.shuffle(traintestdatas[v])


    for i in range(datasplits):
        print("Length of dataset number ", i, " is: ", len(traintestdatas[i]))

    #Store data to file
    for a in range(len(traintestdatas)):
        stringnumber = str(a)
        filename = stringnumber + "teststatickfold.data"
        testfile = open(filename,'w')

        for r in range(len(traintestdatas[a])):
            t = 0
            for item in traintestdatas[a][r]:
                if t < len(traintestdatas[a][r])-1:
                    testfile.write("%s" % item)
                    testfile.write(",")
                else:
                    testfile.write("%s" % item)
                t += 1
            testfile.write("\n")
        testfile.close()


        filename = stringnumber + "trainstatickfold.data"
        trainfile = open(filename,'w')
        thistrain = []
        for q in range(len(traintestdatas)):
            if q != a:
                for t in range(len(traintestdatas[q])):
                    thistrain.append(traintestdatas[q][t])

        random.shuffle(thistrain)

        for r in range(len(thistrain)):
            t = 0
            for item in thistrain[r]:
                if t < len(thistrain[r])-1:
                    trainfile.write("%s" % item)
                    trainfile.write(",")
                else:
                    trainfile.write("%s" % item)
                t += 1
            trainfile.write("\n")


        print(len(thistrain))
        trainfile.close()


fp.close()


for i in range(len(datainfo)):
    print("Dataset number: ", i, " Wins: ", datainfo[i][0], " ", datainfo[i][0]/(datainfo[i][0]+datainfo[i][1]+datainfo[i][2]), " Losses: ", datainfo[i][1], " ", datainfo[i][1]/(datainfo[i][0]+datainfo[i][1]+datainfo[i][2]), " Draws: ", datainfo[i][2], " ", datainfo[i][2]/(datainfo[i][0]+datainfo[i][1]+datainfo[i][2]))



