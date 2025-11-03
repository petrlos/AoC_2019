#Advent of Code 2019: Day 7

from itertools import permutations

def int_code(ns, in_val):
    #opcodes   x 1 2 3 4 5 6 7 8
    lengths = [0,4,4,2,2,3,3,4,4]
    output = []
    ip = 0
    inp_iter = iter(in_val)
    while True:
        opc = ns[ip]
        mode = [opc // (10**i) % 10 for i in range(2, 5)] #0 for position mode, 1 for immediate mode
        opc = opc % 100
        if opc == 99 or ip > len(ns):
            return output[-1]
        param = [ns[ip+i] for i in range(1, lengths[opc]) ] #parameteres
        what = [par if mode[i] else ns[par] for i, par in enumerate(param)]
        if opc == 1: #add up
            ns[ns[ip + 3]] = what[0] + what[1]
        elif opc == 2: #multiple
            ns[ns[ip + 3]] = what[0] * what[1]
        elif opc == 3: #input
            ns[ns[ip+1]] = next(inp_iter)
        elif opc == 4: #output
            output.append(what[0])
        elif opc == 5: #jump if true
            if what[0] != 0: ip = what[1] - 3
        elif opc == 6: #jump if false
            if what[0] == 0: ip = what[1] - 3
        elif opc == 7: #less than
            ns[ns[ip + 3]] = 1 if what[0] < what[1]else 0
        elif opc == 8: #equals
            ns[ns[ip + 3]] = 1 if what[0] == what[1]else 0
        ip += lengths[opc]

#MAIN
with open("data.txt") as file:
    numbers = list(map(int, file.read().split(",")))

sequences = permutations(range(0,5))

result = 0
for sequence in sequences:
    output = 0
    for seq in sequence:
        output = int_code(numbers, [seq, output])
    result = max(result, output)

print("Part 1:", result)