# Advent of Code 2019 - Day 1
from Spaceship import SpaceShipModule

textFile = open("data.txt", "r")
ships = []
for textImport in textFile:
    line = int(textImport)
    ships.append(SpaceShipModule(line))
textFile.close()

#Task1: Total Fuel needed:
suma = 0
for ship in ships:
    suma += ship.fuelNeeded
print("Task1: Total fuel needed: {0}".format(suma))

#Task2: Fuel for fuel needed:
suma = 0
for ship in ships:
    suma += ship.countFuelForFuel()

print("Task2: Total fuel needed: {0}".format(suma))
