#Advent of Code 2019: Day 7 Part 2
from icecream import ic
from itertools import permutations

def int_code(ns, inp_val, ip):
    #opcodes   x 1 2 3 4 5 6 7 8
    lengths = [0,4,4,2,2,3,3,4,4]
    output = []
    inp_iter = iter(inp_val)
    while True:
        opc = ns[ip]
        mode = [opc // (10**i) % 10 for i in range(2, 5)] #0 for position mode, 1 for immediate mode
        opc = opc % 100
        if opc == 99 or ip > len(ns):
            return ns, output, ip, True
        param = [ns[ip+i] for i in range(1, lengths[opc]) ] #parameteres
        what = [par if mode[i] else ns[par] for i, par in enumerate(param)]
        if opc == 1: #add up
            ns[ns[ip + 3]] = what[0] + what[1]
        elif opc == 2: #multiple
            ns[ns[ip + 3]] = what[0] * what[1]
        elif opc == 3: #input
            ns[ns[ip+1]] = next(inp_iter)
        elif opc == 4: #output
            ip += 2 #ip must be increased here - after output it never reaches end of intcode
            return ns, what[0], ip, False
        elif opc == 5: #jump if true
            if what[0] != 0: ip = what[1] - 3
        elif opc == 6: #jump if false
            if what[0] == 0: ip = what[1] - 3
        elif opc == 7: #less than
            ns[ns[ip + 3]] = 1 if what[0] < what[1]else 0
        elif opc == 8: #equals
            ns[ns[ip + 3]] = 1 if what[0] == what[1]else 0
        ip += lengths[opc]

def test_sequence(sequence, numbers):
    outputs = []
    halt = False
    inputs = []
    amplifiers = []
    for i, seq  in enumerate(sequence):
        # numbers, input, ip
        new_amplifier = (numbers[:], None, 0)
        inputs.append([seq]) #initialize first round of inputs with sequence setting
        amplifiers.append(new_amplifier)
    inputs[0].append(0) #first amplifier starts with sequence and input 0
    while not halt:
        for i in range(5):
            ns, _ , ip = amplifiers[i]
            ns, output, ip, halt = int_code(ns, inputs[i], ip)
            amplifiers[i] = (ns[:], None, ip) #store state for next round
            inputs[(i + 1) % 5].append(output) #output from current is the next input
            inputs[i] = [] #reset current input
        if isinstance(output, int): outputs.append(output)
        if halt: return max(outputs)

#MAIN
with open("data.txt") as file:
    numbers = list(map(int, file.read().split(",")))

sequences = permutations(range(5,10))

result = 0
for sequence in sequences:
    max_output = test_sequence(sequence, numbers)
    result = max(result, max_output)

print("Part 2:", result)