#Advent of Code 2019 - Day 6
def countPossibleOrbits(key, orbitMap):
    if not orbitMap[key] == "COM":
        counter.append(1)
        countPossibleOrbits(orbitMap[key], orbitMap)
    else:
        counter.append(1)

with open("test.txt", "r") as file:
    lines = file.read().splitlines()

orbitMap = {}
for line in lines:
    pair = line.split(")")
    orbitMap.setdefault(pair[1], pair[0])

orbitCount = 0
for key in orbitMap.keys():
    counter = []
    countPossibleOrbits(key, orbitMap)
    orbitCount += sum(counter)

print("Task 1:",orbitCount)