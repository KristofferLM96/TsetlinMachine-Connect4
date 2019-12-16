shape_y = 6
shape_x = 7
shape_z = 2
window_x = 4
window_y = 4


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
        return "#"
    elif int(input[2]) and int(input[3]):
        return "b"
    elif int(input[0]):
        return "+X"
    elif int(input[1]):
        return "+O"
    elif int(input[2]):
        return "-x"
    elif int(input[3]):
        return "-o"
    else:
        return "*"


def GetOutput(tm, tm_class, clause):
    output = []
    xyz_id_old = 0
    for i in range(5):
        print(tm.ta_action(tm_class, clause, i))
    for y in range(window_y):
        for x in range(window_x):
            for z in range(shape_z):
                xyz_id = (shape_x - window_x) + (shape_y - window_y) + (y * window_x * shape_z) + (x * shape_z) + z
                output_bit = tm.ta_action(tm_class, clause, xyz_id)
                print("Non-Negated")
                print(xyz_id)
                output.append(output_bit)
                xyz_id_old = xyz_id + 1
    output_pos_neg = GetOutput_negated(tm, tm_class, clause, xyz_id_old, output)
    return output_pos_neg


def GetOutput_negated(tm, tm_class, clause, xyz_id_old, output):
    for y in range(window_y):
        for x in range(window_x):
            for z in range(shape_z):
                xyz_id = xyz_id_old + (shape_x - window_x) + (shape_y - window_y) + (y * window_x * shape_z) \
                         + (x * shape_z) + z
                output_bit = tm.ta_action(tm_class, clause, xyz_id)
                print("Negated")
                print(xyz_id)
                output.append(output_bit)
    return output


def Align(tm, tm_class, clause):
    output = GetOutput(tm, tm_class, clause)
    print(output)
    nonNegated = output[:int(len(output) / 2)]
    negated = output[int(len(output) / 2):]
    xbit = Rearrange(nonNegated[:int(len(nonNegated) / 2)])
    obit = Rearrange(nonNegated[int(len(nonNegated) / 2):])
    nxbit = Rearrange(negated[:int(len(negated) / 2)])
    nobit = Rearrange(negated[int(len(negated) / 2):])
    board = []
    for i in range(window_x * window_y):
        print(i)
        # resultclauses.write(str(xbit[i]) + str(obit[i]) + str(nxbit[i]) + str(nobit[i]))
        if i < (window_x * window_y) - 1:
            resultclauses.write(",")
        else:
            resultclauses.write("\n")


def PrintClause(clause):
    for i in clause:
        print(i)


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

