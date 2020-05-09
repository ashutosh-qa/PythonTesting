# Read the file and store all the lines in list
# Reverse the list (all lines)
# Write the list back to the text file

# With below 1st line, can open file in read mode and put in reader
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


