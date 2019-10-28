import random

file_path = "Data/original/connect-4.data"
file = open(file_path)

binary_file_path = "Data/new/binary.data"
binary_file = open(binary_file_path, "w+")

binary_file_draw_path = "Data/new/binary_draw.data"
binary_file_draw = open(binary_file_draw_path, "w+")

even_train_path = "Data/new/even_train.data"
even_train = open(even_train_path, "w+")

even_train_draw_path = "Data/new/even_train_draw.data"
even_train_draw = open(even_train_draw_path, "w+")

even_test_path = "Data/new/even_test.data"
even_test = open(even_test_path, "w+")

even_test_draw_path = "Data/new/even_test_draw.data"
even_test_draw = open(even_test_draw_path, "w+")


k_fold = 10  # Amount of folds in k-fold distribution
parts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data_binary = []  # Contains data in binary excluding draw
data_binary_draw = []  # Contains all data in binary
ratio = 0.9  # Distribution ratio ex. 0.9 => 90/10 split
data_win = []  # Contains all win-data
data_loss = []  # Contains all loss-data
data_draw = []  # Contains all draw-data

# ***************************************************************************************
# *********************************** FUNCTIONS *****************************************
# ***************************************************************************************


# Function for shuffling data.
# Input: File to shuffle.
# Takes the file and read lines.
# It then shuffles the lines before it writes back the lines to the file.
def shuffle(file):
    lines = file.readlines()
    random.shuffle(lines)
    file.writelines(lines)


# Function to create binary data from original dataset.
# Input: original file(*Not path)
def binary_generator(original_file):
    for line in original_file:
        data_original = line.split(",")
        # Two versions:
        # One WITH draw.
        # One WITHOUT draw.
        # TODO: Optimize code
        for i in data_original:
            if "d" not in i:
                # Checks the list for the positions player x has played.
                # player x has a chip at location i => 1
                # player o has NOT a chip at location i => 0
                for j1 in data_original:
                    if j1 == "x":
                        data_binary.append(1)
                    elif j1 == "o" or j1 == "b":
                        data_binary.append(0)
                # Checks the list for the positions player 0 has played
                # player o has a chip at location j => 1
                # player x has NOT a chip at location j => 0
                for k1 in data_original:
                    if k1 == "o":
                        data_binary.append(1)
                    elif k1 == "x" or k1 == "b":
                        data_binary.append(0)
                # Checks whether the game was a win/loss and replaces it with binary counterpart.
                # win = 1
                # loss = 0
                for l1 in data_original:
                    if "i" in l1:
                        data_binary.append(1)
                    elif "l" in l1:
                        data_binary.append(0)
                # Create file for binary dataset.
                m1 = 1
                for m in data_binary:
                    if m1 < len(data_binary):
                        binary_file.write(str(m) + ",")
                    else:
                        binary_file.write(str(m))
                    m1 += 1
                binary_file.write("\n")

            else:
                # Checks the list for the positions player x has played.
                # player x has a chip at location i => 1
                # player o has NOT a chip at location i => 0
                for j2 in data_original:
                    if j2 == "x":
                        data_binary_draw.append(1)
                    elif j2 == "o" or j2 == "b":
                        data_binary_draw.append(0)
                # Checks the list for the positions player 0 has played
                # player o has a chip at location j => 1
                # player x has NOT a chip at location j => 0
                for k2 in data_original:
                    if k2 == "o":
                        data_binary_draw.append(1)
                    elif k2 == "x" or k2 == "b":
                        data_binary_draw.append(0)
                # Checks whether the game was a win/loss/draw and replaces it with binary counterpart.
                # draw = 2
                # win = 1
                # loss = 0
                for l2 in data_original:
                    if "d" in l2:
                        data_binary_draw.append(2)
                    elif "i" in l2:
                        data_binary_draw.append(1)
                    elif "l" in l2:
                        data_binary_draw.append(0)
                # Create file for binary dataset including draw.
                m2 = 1
                for m in data_binary_draw:
                    if m2 < len(data_binary_draw):
                        binary_file_draw.write(str(m) + ",")
                    else:
                        binary_file_draw.write(str(m))
                    m2 += 1
                binary_file_draw.write("\n")


# Function to evenly distribute the data for train/test.
def even_distribution(file_with_draw):
    for line in file_with_draw:
        line_data = line.split(",")
        if line_data[83] == 2:  # win/loss/draw status is at place 84(index 83).
            data_draw.append(line_data)
        elif line_data[83] == 1:
            data_win.append(line_data)
        elif line_data[83] == 0:
            data_loss.append(line_data)
    amount_win_train = len(data_win) * ratio
    amount_loss_train = len(data_loss) * ratio
    amount_draw_train = len(data_draw) * ratio
    # WIN
    i = 1
    train = True
    if i > amount_win_train:
        train = False
    for value in data_win:
        if i < len(data_win):
            if train:
                even_train.write(str(value) + ",")
                even_train_draw.write(str(value) + ",")
            else:
                even_test.write(str(value) + ",")
                even_test_draw.write(str(value) + ",")
        else:
            if train:
                even_train.write(str(value))
                even_train_draw.write(str(value))
            else:
                even_test.write(str(value))
                even_test_draw.write(str(value))
        i += 1
    if train:
        even_train.write("\n")
        even_train_draw.write("\n")
    else:
        even_test.write("\n")
        even_test_draw.write("\n")
    # LOSS
    j = 1
    train = True
    if j > amount_loss_train:
        train = False
    for value in data_loss:
        if j < len(data_loss):
            if train:
                even_train.write(str(value) + ",")
                even_train_draw.write(str(value) + ",")
            else:
                even_test.write(str(value) + ",")
                even_test_draw.write(str(value) + ",")
        else:
            if train:
                even_train.write(str(value))
                even_train_draw.write(str(value))
            else:
                even_test.write(str(value))
                even_test_draw.write(str(value))
        j += 1
    if train:
        even_train.write("\n")
        even_train_draw.write("\n")
    else:
        even_test.write("\n")
        even_test_draw.write("\n")
    # DRAW
    k = 1
    train = True
    if k > amount_draw_train:
        train = False
    for value in data_draw:
        if k < len(data_draw):
            if train:
                even_train_draw.write(str(value) + ",")
            else:
                even_test_draw.write(str(value) + ",")
        else:
            if train:
                even_train_draw.write(str(value))
            else:
                even_test_draw.write(str(value))
        k += 1
    if train:
        even_train_draw.write("\n")
    else:
        even_test_draw.write("\n")

    shuffle(even_train)
    shuffle(even_test)
    shuffle(even_train_draw)
    shuffle(even_test_draw)


# Function for creating k-fold dataset.
# def k_fold_dataset_generator():



# ***************************************************************************************
# ************************************** MAIN *******************************************
# ***************************************************************************************
binary_generator(file)
even_distribution(binary_file_draw)

file.close()
binary_file.close()
even_train.close()
even_train_draw.close()
even_test.close()
even_test_draw.close()
