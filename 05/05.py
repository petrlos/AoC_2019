#Advent of Code 2019 Day 2

def intCodeProgramm(instructions, inputNr):
    def decodeOpcode(number):
        opcode = []
        opcode.append(number % 100)  # celociselny zbytek po vydeleni 100 je opcode
        numberStr = str(number).rjust(5, "0")  # doplni do cisla nuly na pocet znaku 5
        for i in range(2, -1, -1):
            opcode.append(int(numberStr[i]))
        return opcode

    #opcode:  X 1 2 3 4 5 6 7 8
    offset = [0,4,4,2,2,3,3,4,4]
    currentPosition = 0
    output = []
    while instructions[currentPosition] != 99:
        opcIndex = [] #zde jsou ulozeny INDEXY hodnot
        opcode = decodeOpcode(instructions[currentPosition])
        for i in range(1,offset[opcode[0]]):
            if opcode[i] == 0: #parameter mode - vraci hodnotu na indexu v hodnote
                parameter = instructions[currentPosition+i]
            else: #vraci aktualni hodnotu
                parameter = currentPosition+i
            opcIndex.append(parameter)
        currentPosition += offset[opcode[0]]
        if opcode[0] == 1: #soucet
            instructions[opcIndex[2]] = instructions[opcIndex[0]] + instructions[opcIndex[1]]
        elif opcode[0] == 2: #soucin
            instructions[opcIndex[2]] = instructions[opcIndex[0]] * instructions[opcIndex[1]]
        elif opcode[0] == 3: #input
            instructions[opcIndex[0]] = inputNr
        elif opcode[0] == 4: #output
            output.append(instructions[opcIndex[0]])
        elif opcode[0] == 5: #jump if true - neni roven nule
            if instructions[opcIndex[0]] != 0:
                currentPosition = instructions[opcIndex[1]]
        elif opcode[0] == 6: #jump if false - je roven nule
            if instructions[opcIndex[0]] == 0:
                currentPosition = instructions[opcIndex[1]]
        elif opcode[0] == 7: #is less
            #pokud je prvni cislo mensi nez druhe ulozi jednicku, jinak 0
            if instructions[opcIndex[0]] < instructions[opcIndex[1]]:
                instructions[opcIndex[2]] = 1
            else:
                instructions[opcIndex[2]] = 0
        elif opcode[0] == 8: #is equal
            #pokud jsou dve cisla stejna, ulozi jednicku, jinak 0
            if instructions[opcIndex[0]] == instructions[opcIndex[1]]:
                instructions[opcIndex[2]] = 1
            else:
                instructions[opcIndex[2]] = 0
    return output


#MAIN
with open("test.txt") as file:
    data = file.read()

startInstructions = [int(x) for x in data.split(",")]
task1 = intCodeProgramm(startInstructions, 1)
startInstructions = [int(x) for x in data.split(",")]
task2 = intCodeProgramm(startInstructions, 5)
print("Task 1:", task1)
print("Task 2:", task2[-1])
