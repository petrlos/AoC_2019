def findKeyValueTo(nodes):
    for key in graph.keys():
        if graph[key] == nodes:
            return key

def findNeighbours(starter):
    neighbours = []
    if starter in graph.keys():
        neighbours = graph[starter]
    for nodes in graph.values():
        if starter in nodes:
            newPossibleNeighbour = findKeyValueTo(nodes)
            if newPossibleNeighbour not in visited:
                neighbours.append(newPossibleNeighbour)
    return neighbours

#MAIN

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

graph = {}
for line in lines:
    pair = line.split(")")
    if pair[0] not in graph.keys():
        graph.setdefault(pair[0], [pair[1]])
    else:
        graph[pair[0]].append(pair[1])

start = "YOU"; end = "SAN"
queue = [start]
visited = {start:0}

while end not in queue:
    newNeighbours = findNeighbours(queue[0])
    for neighbour in newNeighbours:
        if neighbour not in visited:
            visited.setdefault(neighbour, visited[queue[0]]+1)
            queue.append(neighbour)
    queue.pop(0)
print("Task 2:", visited[end]-2)