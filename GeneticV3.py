from pyTsetlinMachine.tm import MultiClassTsetlinMachine
import numpy as np
import random

"""
# Parameters
split_ratio = 0.9
train_data = np.loadtxt("bestbinary.data", delimiter=",")

X = train_data[:, 0:-1]
Y = train_data[:, -1]

X_train = X[:int(len(X) * split_ratio)]
X_test = X[int(len(X) * split_ratio):]

Y_train = Y[:int(len(Y) * split_ratio)]
Y_test = Y[int(len(Y) * split_ratio):]
"""

train_data = np.loadtxt("eventrain.data", delimiter=",")
random.shuffle(train_data)
X_train = train_data[:, 0:-1]
Y_train = train_data[:, -1]

test_data = np.loadtxt("eventest.data", delimiter=",")
random.shuffle(train_data)
X_test = test_data[:, 0:-1]
Y_test = test_data[:, -1]


globalhighscore = 0


def smartTsetlin(var1, var2, var3, somepochs, thishighscore):

    tm = MultiClassTsetlinMachine(var1, var2, var3, boost_true_positive_feedback=0)

    tm.fit(X_train, Y_train, epochs=somepochs)

    print(var1," ",var2," ",var3," ",somepochs)
    accuracy = 100*(tm.predict(X_test) == Y_test).mean()
    print("Accuracy:", " ", accuracy)

    #Save shit
    
    if(accuracy > thishighscore):
    
        thishighscore = accuracy
    
        acstr = str(accuracy)
        with open("logsv3.txt", "a+") as myfile:
            myfile.write("var1: " + str(var1) + " var2: " + str(var2) + " var3: " + str(var3) + " epochs: " + str(somepochs) + " accuracy: " + acstr + "\n")
        myfile.close()
        
    return accuracy
  
def dumbScore(var1, var2, var3, somepochs, thishighscore):
    thishighscore = var1 + var2 - var3
    return thishighscore

def generative(individuals, generations, genhighscore):
    #Generation
    individs = []
    for i in range(individuals):
        if i == 0:
            ind = [1538,6,34.52,0]
        elif i == 1:
            ind = [1696,6,33.31,0]
        elif i == 2:
            ind = [1934,10,34.52,0]
        elif i == 3:
            ind = [1700,6,39.27,0]
        elif i == 4:
            ind = [11502,6,39.27,0]
        else:
            var1 = 2* (random.randint(1,1000))
            var2 = random.randint(1,500)
            var3 = round(random.uniform(1,100),2)
            ind = [var1,var2,var3,0]
        individs.append(ind)


    #Live
    for g in range(generations):
        var1 = 2* (random.randint(1,10000))
        var2 = random.randint(1,500)
        var3 = round(random.uniform(1,100),2)
        ind = [var1,var2,var3,0]
        individs.append(ind)
        var1 = 2* (random.randint(1,1000))
        var2 = random.randint(1,200)
        var3 = round(random.uniform(1,50),2)
        ind = [var1,var2,var3,0]
        individs.append(ind)

        tobreed = individs[:]
        breedings = len(tobreed)
        breedings = int(breedings/2)
        
        #Breed
        for w in range(breedings):
            #print("Breed time")
            fatherindex = random.randint(0,len(tobreed)/2)
            fatherdata = tobreed[fatherindex]
            del tobreed[fatherindex]

            motherindex = random.randint(0, int(len(tobreed)/2))
            motherdata = tobreed[motherindex]
            del tobreed[motherindex]

            child1 = fatherdata[:]
            child2 = motherdata[:]
            mutation = random.randint(0,2)

            child1[mutation] = motherdata[mutation]
            child2[mutation] = fatherdata[mutation]
            child1[3] = 0
            child2[3] = 0
            individs.append(child1)
            individs.append(child2)

        #Calculate score/fitness
        for w in range(len(individs)):
            if(individs[w][3] == 0):
                thisscore = smartTsetlin(individs[w][0], individs[w][1], individs[w][2],50,genhighscore)
                #thisscore = dumbScore(individs[w][0], individs[w][1], individs[w][2],50,genhighscore)
                individs[w][3] = thisscore
                if thisscore > genhighscore:
                    genhighscore = thisscore
                
            #individs[w][3] = bet(individs[w][0], individs[w][1], individs[w][2])

            
        
        #Kill half the individs
        while len(individs) > individuals:
            #individs.remove(min(individs[3]))
            lowestscore = 10000000
            lowestindex = 0
            for v in range(len(individs)):
                if individs[v][3] < lowestscore:
                    lowestscore = individs[v][3]
                    lowestindex = v
            del individs[lowestindex]
        for z in range(2):
            lowestscore = 10000000
            lowestindex = 0
            for u in range(len(individs)):
                if individs[u][3] < lowestscore:
                    lowestscore = individs[u][3]
                    lowestindex = u
            del individs[lowestindex]
            
        print("Generation: ", g)
        print(individs)
        
        #Save individuals
        with open("logsv3individuals.txt", "a+") as indfile:
            indfile.write("Generation " + str(g) + "\n" + str(individs) + "\n")
        indfile.close()
        
    bestscore = 0
    bestindex = 0
    for q in range(len(individs)):
        if(individs[q][3] > bestscore):
            bestscore = individs[q][3]
            bestindex = q
    print(individs)
    print("Best stats: ", "var1: ", individs[bestindex][0], " var2: ", individs[bestindex][1], " var3: ", individs[bestindex][2], " Fitness Score: ", individs[bestindex][3])


    
#generative(individuals,generations)
generative(60,30000,globalhighscore)





