# Advent of COde 2019: Day 24
from copy import deepcopy

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def getNeighbours(coords):
    neighbours = 0
    for delta in deltaCoords:
        if tupleSum(delta, coords) in grid:
            neighbours += 1
    return neighbours

def countScore(grid):
    result = 0
    for y in range(5):
        for x in range(5):
            if (x,y) in grid:
                index = y * 5 + x
                result += 2 ** index
    return result

with open("data.txt") as file:
    data = file.read().splitlines()

deltaCoords = [(0,1), (1,0), (0,-1), (-1,0)]

grid = set()
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "#":
            grid.add((x,y))

newGrid = set()
done =  False
score = []
while not done:
    done = True
    for x in range(5):
        for y in range(5):
            neighbourCount = getNeighbours((x,y))
            if (x,y) in grid :
                if neighbourCount == 1:
                    newGrid.add((x,y))
            else:
                if neighbourCount in [1,2]:
                    newGrid.add((x,y))
    grid = deepcopy(newGrid)
    newGrid = set()
    newScore = countScore(grid)
    if newScore not in score:
        score.append(newScore)
        done = False

print("Task 1:",newScore)