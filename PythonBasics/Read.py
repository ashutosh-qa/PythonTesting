
file = open("test.txt")

# Read all content of the fie]le
# print(file.read())
# Read n number of characters by passing parameter
#print(file.read(7))
# Read one single line
#print(file.readline())
#print(file.readline())

# Print line by line entire text file using WHILE loop
# line = file.readline()
# while line != "":  # here condition is line is not equal to blank
#    print(line)
#    line = file.readline()

# Print line by line entire text file using FOR loop
#realines is able to read all lines and store as list
for line in file.readlines():
    print(line)





file.close()

