filepath = "Data/bitcode-connect-4.data"
output_path = "Data/bitcode-connect-4.data"
file = open(filepath, "r")
data = file.read()
output = open(output_path, "w")
output.write(data[:-1])
file.close()
output.close()
