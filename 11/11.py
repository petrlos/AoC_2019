#Advent of Code 2019: Day 11
from collections import defaultdict
from icecream import ic

def int_code(ns, in_val,ip, rb):
    #opcodes   x 1 2 3 4 5 6 7 8 9
    lengths = [0,4,4,2,2,3,3,4,4,2]
    output = []
    inp_iter = iter(in_val)
    while True:
        opc = ns[ip]
        modes = [opc // (10**i) % 10 for i in range(2, 5)]
        #0 for position mode, 1 for immediate mode, #2 for relative mode
        opc = opc % 100
        if opc == 99:
            return None, ns, ip, rb, True
        # parameters: 1-3 numbers directly related to this opcode
        params = [ns[ip+i] for i in range(1, lengths[opc]) ]
        read = [0, 0, 0] #values, no locations
        write_to = [0,0,0] #locations
        for i in range(len(params)):
            if modes[i] == 0: #possition
                read[i] = ns[params[i]]
                write_to[i] = params[i]
            elif modes[i] == 1: #immediate
                read[i] = params[i]
                #write ie never immediate
            if modes[i] == 2: #relative
                read[i] = ns[params[i]+rb]
                write_to[i] = params[i]+rb
        if opc == 1: #add up
            ns[write_to[2]] = read[0] + read[1]
        elif opc == 2: #multiple
            ns[write_to[2]] = read[0] * read[1]
        elif opc == 3: #input
            ns[write_to[0]] = next(inp_iter)
        elif opc == 4: #output
            return read[0], ns, ip+2, rb, False
            #output.append(read[0])
        elif opc == 5: #jump if true
            if read[0] != 0: ip = read[1] - 3
        elif opc == 6: #jump if false
            if read[0] == 0: ip = read[1] - 3
        elif opc == 7: #less than
            ns[write_to[2]] = 1 if read[0] < read[1] else 0
        elif opc == 8: #equals
            ns[write_to[2]] = 1 if read[0] == read[1] else 0
        elif opc == 9:
            rb += read[0]
        ip += lengths[opc]

class IntcodeComputer:
    def __init__(self, program):
        # store the original program and Intcode function
        self.intcode_func = int_code
        self.ip = 0 #pointer
        self.rb = 0 #relative base
        self.halted = False
        self.ns = defaultdict(int, enumerate(map(int, program)))

    def run_until_output(self, input_value):
        if self.halted:
            return None
        output, self.ns, self.ip, self.rb, self.halted = self.intcode_func(self.ns, input_value, self.ip, self.rb)
        return output

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def let_robot_run(numbers, start_colour):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U R D L (row, col)
    facing = 0
    position = (0, 0)
    colours = defaultdict(int, {(0, 0): start_colour})
    rotate = 0
    robot = IntcodeComputer(numbers)

    while rotate != None:
        input_value = colours[position]
        colours[position] = robot.run_until_output([input_value])
        rotate = robot.run_until_output([])
        if rotate == 0:  # left
            facing = (facing - 1) % 4
        elif rotate == 1:  # right
            facing = (facing + 1) % 4
        position = tuple_sum(position, directions[facing])
    return colours

#MAIN
with open("data.txt") as file:
    numbers = file.read().split(",")

part1 = len(let_robot_run(numbers, 0))
print("Part 1:", part1, "\n")

part2 = let_robot_run(numbers, 1)

screen_print = dict({1: "█", 0: " ", None:" "})
for row in range(6):
    for col in range(50):
        if (row, col) in part2.keys():
            print(screen_print[part2[(row, col)]], end="")
        else:
            print(" ", end="")
    print(" ")