#Advent of Code 2019 Day 2

def opCode1(numbers, instructions):
    instructions[numbers[3]] = instructions[numbers[1]] + instructions[numbers[2]]
    return instructions

def opCode2(numbers, instructions):
    instructions[numbers[3]] = instructions[numbers[1]] * instructions[numbers[2]]
    return instructions

def intCodeProgramm(instructions):
    currentPosition = 0

    while instructions[currentPosition] != 99:
        if instructions[currentPosition] == 1:
            instructions = opCode1(instructions[currentPosition:currentPosition + 4], instructions)
        elif instructions[currentPosition] == 2:
            instructions = opCode2(instructions[currentPosition:currentPosition + 4], instructions)
        currentPosition += 4
    return instructions[0]


#MAIN
with open("data.txt") as file:
    data = file.read()

startInstructions = [int(x) for x in data.split(",")]

data = startInstructions*1

task1 = intCodeProgramm(data)
print("Task 1:", task1)

for noun in range(100):
    for verb in range(100):
        data = startInstructions *1
        data[1] = noun
        data[2] = verb
        task2 = intCodeProgramm(data)
        if task2 == 19690720:
            result = str(noun*100 + verb)
            print("Task 2:",result)
