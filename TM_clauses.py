import csv

shape_y = 6
shape_x = 7


def Rearrange(WrongList):
    output = []
    for column in range(shape_y):
        temp = shape_y - column
        for row in range(shape_x):
            index = (shape_y * row) + temp
            # print(index)
            output.append(WrongList[index - 1])
    return output


def transform(input):
    # print(input)
    if (int(input[0]) and int(input[2])) or (int(input[1]) and int(input[3])):
        return "Fa"
    elif int(input[0]) and int(input[1]):
        return "+#"
    elif int(input[2]) and int(input[3]):
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
    xbit = nonNegated[:int(len(nonNegated) / 2)]
    obit = nonNegated[int(len(nonNegated) / 2):]
    nxbit = negated[:int(len(negated) / 2)]
    nobit = negated[int(len(negated) / 2):]
    board = []
    for i in range(42):
        print(str(xbit[i]) + str(obit[i]) + str(nxbit[i]) + str(nobit[i]))
        if i < 41:
            print(",")
        else:
            print("\n")


def PrintClass(Ts, Class, clauses):
    for i in range(clauses):
        Align(Ts, Class, i)
        # resultclauses.writelines(clausesres)
        # print(clausesres)
        # PrintClause(action)


# PrintClass(tm, 1, clauses)

with open("Data/2D1218-0437clauses1.csv") as f:
    reader = csv.reader(f)
    table = []
    for row in reader:
        table.append(row)
    index = 1
    for index in range(100):
        print(table[index])
        for i in range(6):
            temp = ""
            for j in range(7):
                temp = temp + transform(table[index][i * 7 + j]) + " "
                # print(i*7+j)
            print(temp)
        print("\n")
        index = index + 1
