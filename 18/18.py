#Advenf of Code 2019 Day 18
from icecream import ic
from collections import deque, namedtuple
import heapq

def flood_fill(key, coords):
    visited = {coords: (0, "")} #coords: distance from start, doors visited
    queue = deque([coords])
    new_edges = dict()
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
                new_edges["".join(sorted(key+maze[n_row][n_coll]))] = (dist + 1, set(path))
                continue
            if maze[n_row][n_coll].isupper(): #finds door
                visited[n_row, n_coll] = (dist + 1, path + maze[n_row][n_coll])
                queue.append((n_row, n_coll))
                continue
            queue.append((n_row, n_coll))
            visited[(n_row, n_coll)] = (dist+1, path)
    return new_edges

def find_path(start, all_keys):

    all_keys = set(all_keys)
    all_keys.add("@")
    queue = [(0, start, start)] # distance, position, path
    heapq.heapify(queue)

    while queue:
        dist, pos, path = heapq.heappop(queue)
        if set(path) == all_keys: return dist
        for edge, parameters in edges.items():
            if pos in edge:
                dest = edge.replace(pos, "")
                if dest not in path:  # key not yet picked up
                    added_distance, keys_needed = parameters
                    if len(keys_needed - set(path.upper())) == 0:
                        heapq.heappush(queue, (dist + added_distance, dest, path+dest))

#MAIN
with open("data.txt") as file:
    maze = file.read().splitlines()

#find all keys
keys = dict()
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == "@":
            start = (row, col)
        if maze[row][col].islower():
            keys[maze[row][col]] = (row, col)

#find paths from start to all keys and doors lying on them
edges = flood_fill("@", start)

#find shortest path between each pair of keys and doors lying on them
for key, coords in keys.items():
    new_edges = flood_fill(key, coords)
    for path, parameters in new_edges.items():
        if path not in edges:
            edges[path] = parameters

print(find_path("@", keys.keys()))