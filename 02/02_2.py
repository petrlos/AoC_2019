#Advent of Code 2019: Day 2

def int_code(ns, in_1, in_2):
    ns[1] = in_1
    ns[2] = in_2

    ip = 0
    while True:
        opc = ns[ip]
        if opc == 1: #add up
            ns[ns[ip + 3]] = ns[ns[ip + 1]] + ns[ns[ip + 2]]
            ip += 4
        if opc == 2: #multiple
            ns[ns[ip + 3]] = ns[ns[ip + 1]] * ns[ns[ip + 2]]
            ip += 4
        if opc == 99 or ip > len(ns): break
    return ns[0]

#MAIN
with open("data.txt") as file:
    numbers = list(map(int, file.read().split(",")))

print("Part 1:",int_code(numbers[:], 12,2))

for i in range(100):
    for j in range(100):
        if int_code(numbers[:], i, j) == 19690720:
            print("Part 2:",i*100+j)