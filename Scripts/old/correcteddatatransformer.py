
"""
This script creates a dataset that is transformed in such a way that the tsetlin automata reads it correctly.
"""
print("Correcting board")
import csv
def Rearrange(list):
    output = []
    for column in range(6):
        temp = 6 - column
        for row in range(7):
            index = (6 * row) + temp
            #print(index)
            output.append(list[index - 1])
    output.append(list[42])
    return output


with open("connect-4.data") as File:
    print("opening source")
    reader =csv.reader(File)
    with open("connect4flipped.data", "w", newline='') as csv_file:
        print("opening target")
        writer = csv.writer(csv_file, delimiter=',')
        for row in reader:
            newRow = Rearrange(row)
            writer.writerow(newRow)



print("Transforming to binary")

# Parameters
file_path = "connect4flipped.data"
new_file_path = "flippeddrawbin.data"
file = open(file_path)
new_file = open(new_file_path, "w+")

# Option 1: Goes through every line N in the file.
# Option 2: Goes through every line in the file.
# for line in [next(file) for x in range(N)]:
for line in file:
    # temp list for the binary datalist.
    new_data_line_list = []
    # Adds all the data from the line read into a list.
    # Makes it easier to work with.
    data_line_list = line.split(",")


    # Checks the list for the positions player x has played.
    # player x has a chip at location i => 1
    # player x has NOT a chip at location i => 0
    for j in data_line_list:
        if j == "x":
            new_data_line_list.append(1)
        elif j == "o" or j == "b":
            new_data_line_list.append(0)

    # Checks the list for the positions player 0 has played
    # player o has a chip at location j => 1
    # player x has NOT a chip at location j => 0
    for k in data_line_list:
        if k == "o":
            new_data_line_list.append(1)
        elif k == "x" or k == "b":
            new_data_line_list.append(0)

    # Checks whether the game was a win/loss and replaces it with binary counterpart.
    # win = 1
    # loss = 0
    # draw = 2
    for l in data_line_list:
        if "i" in l:
            new_data_line_list.append(1)
        elif "l" in l:
            new_data_line_list.append(0)
        elif "d" in l:
            new_data_line_list.append(2)

    # print(new_data_line_list)
    ii = 1
    for m in new_data_line_list:
        if ii < len(new_data_line_list):
            new_file.write(str(m) + ",")
        else:
            new_file.write(str(m))
        ii += 1
    new_file.write("\n")

file.close()
new_file.close()


print("Splitting up to 10 sets of train and test data for Kfold validation, where there is an even distribution wins, losses and draws")

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
filepath = "flippeddrawbin.data"
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
        filename = stringnumber + "teststatickfoldcorrected.data"
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


        filename = stringnumber + "trainstatickfoldcorrected.data"
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



