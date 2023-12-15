def hash(string):
    result = 0
    for char in string:
        result += ord(char)
        result *= 17
        result = result % 256
    return result