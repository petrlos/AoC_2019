#Advent of Code 2019: Day 12
import re
from itertools import combinations

class Moon:
    def __init__(self, name, coords):
        self.name = name
        self.location = coords * 1
        self.velocity = [0,0,0]

    def __str__(self):
        return "{0}: {1}, {2}".format(self.name, self.location, self.velocity)

def tupleSum(a,b):
    return [x + y for x, y in zip(a,b)]

#MAIN:
regNum = re.compile(r"-?\d+")
steps = 1000

with open("data.txt") as file:
    data = file.read().splitlines()
moonNames = "io,europa,ganymede,callisto".split(",")
moons = []
for index, line in enumerate(data):
    coords = [int(x) for x in regNum.findall(line)]
    newMoon = Moon(moonNames[index], coords)
    moons.append(newMoon)

for step in range(steps):
    moonPairs = combinations(moons, 2)
    for moon in moonPairs:
        for i in range(3):
            if moon[0].location[i] < moon[1].location[i]:
                moon[0].velocity[i] += 1
                moon[1].velocity[i] -= 1
            elif moon[0].location[i] > moon[1].location[i]:
                moon[0].velocity[i] -= 1
                moon[1].velocity[i] += 1
    for moon in moons:
        newLocation = tupleSum(moon.location, moon.velocity)
        moon.location = newLocation

for moon in moons:
    print(moon)
totalEnergy = 0

for moon in moons:
    potential = sum([abs(x) for x in moon.location])
    kinetic = sum([abs(x) for x in moon.velocity])
    totalEnergy += potential * kinetic

print("Task 1:",totalEnergy)