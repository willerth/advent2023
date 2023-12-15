from util import *

#inputFile = open('day15/example.txt')
inputFile = open('day15/input.txt')
inputText = inputFile.read().split(',')
inputFile.close()


sum = 0
for value in inputText:
    sum += hash(value)

print(sum)