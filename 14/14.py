#Advent of Code 2019: Day 14
from pprint import pprint as pp

def parseData(lines):
    rules = {}
    for line in lines:
        ingred, result = line.split(" => ")
        amount, key = result.split(" ")
        rules_single_line = []
        for ingredient in ingred.split(", "):
            am, ingr = ingredient.split(" ")
            rules_single_line.append((ingr, int(am)))
        rules[key] = (int(amount), rules_single_line)
    return rules

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

rules = parseData(lines)

pp(rules)