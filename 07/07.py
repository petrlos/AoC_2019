#Advent of Code 2019: Intcode Prototype
from itertools import permutations

def intCode(numbers, input):
    numbersList = [int(x) for x in numbers.split(",")]
    numbers = dict()
    for index, number in enumerate(numbersList):
        numbers[index] = number
    # opcode: X  1  2  3  4  5  6  7  8
    offset = [0, 4, 4, 2, 2, 3, 3, 4, 4]
    pointer = 0
    outputs = []
    inputIndex = 0
    while True:
        opCode = numbers[pointer]
        modes = [(opCode // 10 ** i) % 10 for i in range(2, 5)]
        opCode = opCode % 100
        if opCode == 99:
            return outputs
        positions = [numbers[pointer + i] for i in range(1,offset[opCode])]
        parameters = []
        for position, mode in zip(positions, modes):
            if mode == 0: #position mode - vrati cislo, ktere se nachazi na prislusnem indexu
                parameters.append(numbers[position])
            elif mode == 1: #relative mode - vrati primo to cislo
                parameters.append(position)
        pointer += offset[opCode]
        if opCode == 1: #addition
            numbers[positions[2]] = parameters[0] + parameters[1]
        elif opCode == 2: #multiply
            numbers[positions[2]] = parameters[0] * parameters[1]
        elif opCode == 3: #input
            numbers[positions[0]] = input[inputIndex]
            inputIndex += 1
        elif opCode == 4: #output
            outputs.append(parameters[0])
        elif opCode == 5: #jump if true
            if parameters[0] != 0:
                pointer = parameters[1]
        elif opCode == 6: #jump if false
            if parameters[0] == 0:
                pointer = parameters[1]
        elif opCode == 7: #less than
            numbers[positions[-1]] = parameters[0] < parameters[1]
        elif opCode == 8: #equals
            numbers[positions[-1]] = parameters[0] == parameters[1]

#MAIN:

with open("test.txt") as file:
    numbers = file.read()

settings = permutations(range(5), 5)

maxOutput = -1
for setting in settings:
    output = 0
    for input in setting:
        output = intCode(numbers, [input, output])[0]
    if output > maxOutput:
        maxOutput = output
print("Task 1:", maxOutput)

#TODO: Task2 day 7: Thrusters-LOOP