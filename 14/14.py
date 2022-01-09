#Advent of Code 2019: Day 14
#TODO: ORE -> FUEL, only parsing works

import re
def parseData(lines):
    rules = {}
    for line in lines:
        left, right = line.split("=>")
        rules[right] = left.split(",")
    return rules

#MAIN
regNum = re.compile(r"\d+")
with open("test.txt") as file:
    lines = file.read().replace(" ","").splitlines()

rules = parseData(lines)
start = "1FUEL"