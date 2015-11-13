import fileinput
for line in fileinput.input(filename):
    process(line)
	
# do not need to close file
