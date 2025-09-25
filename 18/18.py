#Advenf of Code 2019 Day 18
from icecream import ic
from collections import deque

def flood_fill(key, coords):
    visited = {coords: (0, "")} #coords: distance from start, doors visited
    queue = deque([coords])
    edges = dict()
    while queue:
        row, col = queue.popleft()
        dist, path = visited[(row, col)]
        for n_row, n_coll in ((row - 1, col), (row+1, col), (row, col-1), (row, col + 1)):
            if n_row < 0 or n_row > len(maze): continue #out of bounds - rows
            if n_coll < 0 or n_coll > len(maze[0]): continue #otu of bounds - cols
            if maze[n_row][n_coll] == "#": continue #hit the wall
            if (n_row, n_coll) in visited.keys(): continue #already visited
            if maze[n_row][n_coll].islower(): #finds key
                visited[n_row, n_coll] = (dist + 1, path) #
                queue.append((n_row, n_coll))
                edges["".join(sorted(key+maze[n_row][n_coll]))] = (dist + 1, path)
                continue
            if maze[n_row][n_coll].isupper(): #finds door
                visited[n_row, n_coll] = (dist + 1, path + maze[n_row][n_coll])
                queue.append((n_row, n_coll))
                continue
            queue.append((n_row, n_coll))
            visited[(n_row, n_coll)] = (dist+1, path)
    return edges

#MAIN
with open("test.txt") as file:
    maze = file.read().splitlines()

keys = dict()
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == "@":
            start = (row, col)
        if maze[row][col].islower():
            keys[maze[row][col]] = (row, col)

edges = []

first_step = flood_fill("@", start)
print(first_step)
for key, coords in keys.items():
    new_edges = flood_fill(key, coords)
