from util import *

#inputFile = open('day15/example.txt')
inputFile = open('day15/input.txt')
inputText = inputFile.read().split(',')
inputFile.close()

boxes = {}

for value in inputText:
    labelLength = value.index('-') if '-' in value else value.index('=')
    label = value[:labelLength]
    boxNo = hash(label)
    if boxNo not in boxes.keys(): boxes[boxNo] = []
    box = boxes[boxNo]

    operation = value[labelLength]
    if operation == '-':
        for lens in box:
            if lens[0] == label:
                box.remove(lens)
                #break

    else:
        focalLength = int(value[labelLength + 1])
        labelAlreadyPresent = False
        for lens in box:
            if lens[0] == label:
                lens[1] = focalLength
                labelAlreadyPresent = True
                #break
        if not labelAlreadyPresent:
            box.append([label, focalLength])




sum = 0
for boxNo in boxes.keys():
    multiplier = boxNo + 1
    box = boxes[boxNo]
    position = 1
    for lens in box:
        focalLength = lens[1]
        sum += multiplier * position * focalLength
        position += 1


print(sum)