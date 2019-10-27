file_path = "Data/original/connect-4.data"
file = open(file_path)
k_fold = 10
parts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data_binary = []
data_binary_draw = []
ratio = 0.9  # Distribution ratio ex. 0.9 => 90/10 split

# ***************************************************************************************
# *********************************** FUNCTIONS *****************************************
# ***************************************************************************************


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



# Function to evenly distribute the data for train/test.
def even_distribution():



# Function for creating k-fold dataset.
def k_fold_dataset_generator():



# Function for displaying information about the various dataset lists:
def display_information():



# Function for creating files from the various dataset lists.
def create_files():




# ***************************************************************************************
# ************************************** MAIN *******************************************
# ***************************************************************************************
binary_generator(file)