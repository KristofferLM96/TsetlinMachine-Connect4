# Parameters
file_path = "Data/connect-4.data"
new_file_path = "Data/bitcode-connect-4.data"
N = 7
skip = False
file = open(file_path)
new_file = open(new_file_path, "w+")

# Option 1: Goes through every line N in the file.
# Option 2: Goes through every line in the file.
#for line in [next(file) for x in range(N)]:
for line in file:
    # temp list for the binary datalist.
    new_data_line_list = []
    # Adds all the data from the line read into a list.
    # Makes it easier to work with.
    data_line_list = line.split(",")

    # Checks whether the game ending was draw.
    # Set skip flag as true if draw.
    for i in data_line_list:
        if "d" in i:
            skip = True
        else:
            skip = False

    if skip is False:
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
        for l in data_line_list:
            if "i" in l:
                new_data_line_list.append(1)
            elif "l" in l:
                new_data_line_list.append(0)

        #print(new_data_line_list)
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
