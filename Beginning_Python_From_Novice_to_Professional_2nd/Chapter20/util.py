def lines(file):
    for line in file: yield line
    yield '\n'

# how to seperate block ??? if block is not empty, yield and initialize it
# how to deal with the empty line?
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []