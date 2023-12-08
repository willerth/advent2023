import time

startTime = time.time()

#INPUT HANDLING
inputFile = open('day06/input.txt')
inputTxt = inputFile.read().split(':')[1:]
inputFile.close()

times = inputTxt[0].strip().split()[:-1]
distances = inputTxt[1].split()


timeAllowed = int(("".join(times)))
distance = int(("".join(distances)))
possibilities = 0
for j in range(timeAllowed):
    holdTime = j
    moveTime = timeAllowed - j
    distTraveled = holdTime * moveTime
    if distTraveled > distance:
        possibilities += 1

print(possibilities)
print(f'Code executed in {time.time() - startTime} seconds')
exit()

#MAIN SECTION
result = 1
for i in range(len(times)):
    possibilities = 0
    timeAllowed = times[i]
    for j in range(timeAllowed):
        holdTime = j
        moveTime = timeAllowed - j
        distTraveled = holdTime * moveTime
        if distTraveled > distances[i]:
            possibilities += 1
    
    result *= possibilities

print(result)