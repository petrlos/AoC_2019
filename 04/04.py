from datetime import datetime
#Advent of Code 2019 - Day 4

def numbersSorted(number):
    # cisla musi byt po sobe jdouci
    numberStr = str(number)
    numberStrSorted = "".join(sorted(numberStr))
    return numberStr == numberStrSorted

def twoDigitsTask1(number):
    # dve vedle sebe stojici cisla musi byt stejna
    numberStr = str(number)
    result = False
    for i in range(1,len(numberStr)):
        if numberStr[i-1] == numberStr[i]:
            result = True
    return result

def twoDigitsTask2(number):
    numberStr = str(number)
    result = False
    for i in range(1,len(numberStr)):
        if numberStr[i-1] == numberStr[i] and numberStr.count(numberStr[i]) == 2:
            result = True
    return result

## MAIN

start = datetime.now()
countTask1, countTask2 = 0, 0
for i in range(156218, 652527, 1):
    if numbersSorted(i):
        if twoDigitsTask1(i):
            countTask1 += 1
        if twoDigitsTask2(i):
            countTask2 += 1

print("Task1: {0} valid passwords".format(countTask1))
print("Task2: {0} valid passwords".format(countTask2))

print("Runtime:",datetime.now()-start)