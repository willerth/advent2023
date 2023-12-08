#INPUT HANDLING
inputFile = open('day06/input.txt')
inputTxt = inputFile.read().split(':')[1:]
inputFile.close()

times = inputTxt[0].strip().split()[:-1]
distances = inputTxt[1].split()
for i in range(len(times)):
    times[i] = int(times[i])
    distances[i] = int(distances[i])


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