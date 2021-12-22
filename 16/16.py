#Advent of Code 2019 Day 16

def getNewPattern(pattern, index):
    result = []
    for number in pattern:
        result += [number] * index
    return result

#MAIN:

with open("data.txt") as file:
    input = file.read()

input = [int(x) for x in input]
startPattern = [0,1,0,-1]


for phase in range(0,100):
    result = []
    for i in range(1, len(input)+1):
        pattern = getNewPattern(startPattern, i)
        newPosition = 0
        for index, number in enumerate(input):
            newPosition += pattern[(index+1) % len(pattern)] * number
        result.append(int(str(newPosition)[-1:]))
    input = result * 1
    if phase % 10 == 0:
        print("{0}% task1 done".format(phase))
print("Task 1:", "".join([str(x) for x in result[:8]]))