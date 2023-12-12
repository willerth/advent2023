def transposed(list):
    numColumns = len(list[0])
    result = []
    for i in range(numColumns):
        result.append([])
        for j in range(len(list)):
            result[i].append(list[j][i])
        
        result[i] = ''.join(result[i])

    return result

def expand(universe):
    result = []
    for line in universe:
        result.append(line.strip())
        if '#' not in line:
            result.append(line.strip())
    
    return result

