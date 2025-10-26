#Advent of Code 2019: Day 20
from icecream import ic
from collections import deque

def search_for_portals(lines):
    portals = dict()
    letters = dict()
    maze = dict()
    for row, line in enumerate(lines):
        for col, letter in enumerate(line):
            if letter in '# ': continue
            maze[row, col] = letter
            if letter.isalpha():
                letters[(row, col)] = letter
    for coords, letter in letters.items():
        row, col = coords
        for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if (n_row, n_col) not in letters.keys(): continue
            for d_row, d_col in [(n_row - 1, n_col), (n_row +1 , n_col), (n_row, n_col + 1), (n_row, n_col - 1)]:
                if (d_row, d_col) not in maze.keys(): continue
                if maze[(d_row, d_col)] == ".":
                    if row == n_row: #horizontal
                        if col < n_col:
                            portal = letter + maze[(n_row, n_col)]
                        else:
                            portal = maze[(n_row, n_col)] + letter
                        if portal not in portals: portals[portal] = []
                        portals[portal].append((d_row, d_col))
                        portals[(d_row, d_col)] = portal
                    else: #vertical
                        if row < n_row:
                            portal = letter + maze[(n_row, n_col)]
                        else:
                            portal = maze[(n_row, n_col)] + letter
                        if portal not in portals: portals[portal] = []
                        portals[portal].append((d_row, d_col))
                        portals[(d_row, d_col)] = portal
    return portals, maze

def bfs(maze, portals, start, target):
    ic(portals)
    queue = deque([start])
    visited = dict({start: 0})
    while queue:
        row, col = queue.popleft()
        for n_row, n_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if (n_row, n_col) not in maze.keys() or maze[(n_row, n_col)] == " ": continue
            if maze[(n_row, n_col)] != "." and maze[(n_row, n_col)].isalpha():
                if (row, col) not in portals: continue
                portal_in = portals[(row, col)]
                if len(portals[portal_in]) == 1: continue
                portal_out = portals[portal_in][1] if portals[portal_in][0] == (row, col) else portals[portal_in][0]
                n_row, n_col = portal_out
            if (n_row, n_col) in visited.keys(): continue
            queue.append((n_row, n_col))
            visited[(n_row, n_col)] = visited[(row, col)] + 1
            if (n_row, n_col) == target:
                return visited[target]

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

portals, maze = search_for_portals(lines)

start = portals["AA"][0]
target = portals["ZZ"][0]

result = bfs(maze, portals, start, target)
print(result)