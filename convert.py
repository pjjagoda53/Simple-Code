""" Takes a file as input, reads the first line as an int and outputs a second file with int squared
"""

inputFile = 'file1.txt'

with open(inputFile, 'r') as f:
    inputInt = int(f.readline())

outputFile = 'file2.txt'

outputInt = inputInt**2

with open(outputFile, 'w') as f:
    f.write(str(outputInt))

print('Wrote {} ({}^2) to {}'.format(outputInt, inputInt, outputFile))

