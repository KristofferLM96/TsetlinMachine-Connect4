def Rearrange(WrongList):
    output = []
    for column in range(6):
        temp = 6 - column
        for row in range(7):
            index = (6 * row) + temp
            # print(index)
            output.append(WrongList[index - 1])
    return output


def transform(input):
    # print(input)
    if (int(input[0]) and int(input[2])) or (int(input[1]) and int(input[3])):
        return "Fa"
    elif (int(input[0]) and int(input[1])):
        return "+#"
    elif (int(input[2]) and int(input[3])):
        return "-#"
    elif int(input[0]):
        return "+X"
    elif int(input[1]):
        return "+O"
    elif int(input[2]):
        return "-x"
    elif int(input[3]):
        return "-o"
    else:
        return "*#"


def GetOutput(tm, tm_class, clause):
    output = []
    for i in range(84 * 2):
        outputbit = tm.ta_action(tm_class, clause, i)
        output.append(outputbit)
    return output


def PrintClause(clause):
    for i in clause:
        print(i)


def Align(tm, tm_class, clause):
    output = GetOutput(tm, tm_class, clause)
    nonNegated = output[:int(len(output) / 2)]
    negated = output[int(len(output) / 2):]
    xbit = Rearrange(nonNegated[:int(len(nonNegated) / 2)])
    obit = Rearrange(nonNegated[int(len(nonNegated) / 2):])
    nxbit = Rearrange(negated[:int(len(negated) / 2)])
    nobit = Rearrange(negated[int(len(negated) / 2):])
    board = []
    for i in range(42):
        resultclauses.write(str(xbit[i]) + str(obit[i]) + str(nxbit[i]) + str(nobit[i]))
        if i < 41:
            resultclauses.write(",")
        else:
            resultclauses.write("\n")


def PrintClass(Ts, Class, clauses):
    for i in range(clauses):
        Align(Ts, Class, i)
        # resultclauses.writelines(clausesres)
        # print(clausesres)
        # PrintClause(action)


PrintClass(tm, 1, clauses)
resultclauses.close()

with open("3Dresults/2D" + timestr + "clauses.csv") as f:
    reader = csv.reader(f)
    table = []
    for row in reader:
        table.append(row)
    print(table[1])
    for i in range(6):
        temp = ""
        for j in range(7):
            temp = temp + transform(table[1][i * 7 + j]) + " "
            # print(i*7+j)
        print(temp)