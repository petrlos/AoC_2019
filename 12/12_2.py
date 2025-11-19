#Advent of Code 2019: Day 12
import re
from math import gcd

def move_moons(coords):
    start_coords = coords[:]
    vel = [0,0,0,0]
    counter = 0
    while True:
        for i, coord in enumerate(coords):
            for j in range(4):
                if coords[j] > coord: #coord is higher: velocity increase by 1
                    vel[i] += 1
                elif coords[j] < coord: #coord is lower: velocity decrease by 1
                    vel[i] -= 1
        for i in range(4):
            coords[i] = coords[i] + vel[i]
        counter += 1
        #if all velocities == 0 and coords are same as start
        if set(vel) == {0} and coords == start_coords:
            return counter

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

moons = []
for line in lines:
    numbers = list(map(int,(re.findall(r"-?\d+",line))))
    moons.append(numbers)

start_state = []
for i in range(3): #get all x-coords, y and z and find start state
    coords = []
    for c in moons:
        coords.append(c[i])
    start_state.append(move_moons(coords))

result = lcm(start_state[0], start_state[1]) #LCM of first two
result = lcm(result, start_state[2]) #LCM of (first two) and third

print("Part 2:", result)