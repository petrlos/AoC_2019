#Advent of Code 2019 Day 10
def greatestCommonDivisor(gradX, gradY):
    gcd = 1
    for i in range(1,min([abs(gradX), abs(gradY)])+1):
        if gradX % i == 0 and gradY % i == 0:
            gcd = i
    return gradX // gcd, gradY // gcd

def visible(stationX, stationY, visX, visY):
    gradX = visX - stationX
    gradY = visY - stationY
    if gradX == 0 or gradY == 0:
        if gradX == 0:
            gradY = gradY // abs(gradY)
        else:
            gradX = gradX // abs(gradX)
    else:
        gradX, gradY = greatestCommonDivisor(gradX, gradY)
    searchedX = stationX; searchedY = stationY
    while True:
        searchedX += gradX
        searchedY += gradY
        if searchedX == visX and searchedY == visY:
            break
        if field[searchedX][searchedY] != ".":
            return False
    return True

def countVisible(stationX, stationY):
    counter = 0
    for visX in range(len(field[0])):
        for visY in range(len(field)):
            if field[visX][visY] != "." and (stationX != visX or stationY != visY):
                if visible(stationX, stationY, visX, visY):
                    counter += 1
    return counter

#MAIN
with open("data.txt", "r") as file:
    field = [list(x) for x in file.read().splitlines()]

for row in range(len(field[0])):
    for col in range(len(field)):
        if field[row][col] != ".":
            field[row][col] = countVisible(row, col)

result = []
for line in field:
    for asteroid in line:
        if asteroid != ".":
           result.append(asteroid)

print("Task 1:",max(result))