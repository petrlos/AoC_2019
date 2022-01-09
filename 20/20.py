#Advent of Code 2019: Day 20

from collections import deque
def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def getNeighbours(coords):
    neighbours = []
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # UDLR
    for direction in directions:
        possibleNeighbour = tupleSum(direction, coords)
        if possibleNeighbour in maze.keys():
            if maze[possibleNeighbour] == ".":
                neighbours.append(possibleNeighbour)
    return neighbours

with open("test.txt") as file:
    lines = file.read().splitlines()

maze = {}
for row, line in enumerate(lines):
    for column, char in enumerate(line):
        maze[(row, column)] = char
maxRow = row
maxColumn = column

#TODO: parse portals, BFS is ready and working
portals = {}
for coords, char in maze.items():
    if char.isalpha():
        row, column = coords



start = (2,9)
queue = deque([start])
distances = {start:0}

while queue:
    neighbours = getNeighbours(queue[0])
    for neighbour in neighbours:
        if neighbour not in distances.keys():
            distances[neighbour] = distances[queue[0]] + 1
            queue.append(neighbour)
    queue.popleft()

end = (16,13)
print(distances[end])