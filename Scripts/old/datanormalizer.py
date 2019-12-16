import math
import random

""" This script splits a binary data file into a train and 
test datafile which are almost evenly distributed in terms of wins and losses """

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

trnd = open('xeventrain.data', 'w')
tstd = open('xeventest.data', 'w')
"""Filepath refers to data file in binary form"""
filepath = "bestbinary.data"
with open(filepath) as fp:
    line = fp.readline()
    wins = []
    losses = []
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
        else:
            print("Not win nor loss")

    #print("Wins ", wins)
    #print("Losses ", losses)
    print("Amount of wins: ", len(wins))
    print("Amount of losses: ", len(losses))

    trainlosses = 0
    testlosses = 0
    trainwins = 0
    testwins = 0

    traindata = []
    testdata = []
    split = 0.9
    splitwin = round_down(len(wins)*split)
    splitloss = round_down(len(losses)*split)
    #ratio = round_down(len(wins)/len(losses))
    trainwin = round_down(len(wins)*split)
    trainloss = round_down(len(losses)*split)
    #testwin = len(wins) - trainwin
    #testloss = len(losses) - trainloss
    for e in range(len(wins)):
        if e < trainwin:
            #print("train")
            #traindata.append(losses[e])
            traindata.append(wins[e])
            trainwins += 1
        else:
            #print("test")
            #testdata.append(losses[e])
            testdata.append(wins[e])
            testwins += 1
    for e in range(len(losses)):
        if e < trainloss:
            #print("train")
            traindata.append(losses[e])
            #traindata.append(wins[e])
            trainlosses += 1

        else:
            #print("test")
            testdata.append(losses[e])
            #testdata.append(wins[e])
            testlosses += 1

    random.shuffle(traindata)
    random.shuffle(testdata)
    print("Length of traindata ", len(traindata))
    print("Length of testdata ", len(testdata))

    for r in range(len(traindata)):
        t = 0
        for item in traindata[r]:
            if t < len(traindata[r])-1:
                trnd.write("%s" % item)
                trnd.write(",")
            else:
                trnd.write("%s" % item)
            t += 1
        trnd.write("\n")
    for r in range(len(testdata)):
        t = 0
        for item in testdata[r]:
            if t < len(testdata[r])-1:
                tstd.write("%s" % item)
                tstd.write(",")
            else:
                tstd.write("%s" % item)
            t += 1
        tstd.write("\n")


print("Training: Wins: ", trainwins, " Losses: ", trainlosses, " Ratio: ", trainwins/trainlosses)
print("Testing: Wins: ", testwins, " Losses: ", testlosses, " Ratio: ", testwins/testlosses)
fp.close()
trnd.close()
tstd.close()

