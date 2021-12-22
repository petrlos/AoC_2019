# Advent of Code 2019 - Day 3
from cable import Cable

textFile = open("data.txt", "r")
kabely = []
for textImport in textFile:
    kabel = Cable(textImport[:-1].split(","))
    kabely.append(kabel)
textFile.close()

for kabel in kabely:
    kabel.getPath()
    print("Kabel ready")

#find intersections
# https://www.geeksforgeeks.org/python-intersection-two-lists/ metoda 3
intersections = set(kabely[0].path).intersection(kabely[1].path)

#TASK 1: spocitej nejmensi vzdalenosti
distanceTask1 = []
for intersection in intersections:
    distanceTask1.append(abs(intersection[0])+abs(intersection[1]))
print("Task1: Minimal manhattan distance to intersection: {0}".format(min(distanceTask1)))
#TASK2 - najdi nejkratsi vzdalenost kabelu k intersection

distanceTask2 = []
for intersection in intersections:
    index1 = kabely[0].path.index(intersection) + 1
    index2 = kabely[1].path.index(intersection) + 1
    distanceTask2.append(index1 + index2)

print("Task2: Minimal cable length to intersection: {0}".format(min(distanceTask2)))
