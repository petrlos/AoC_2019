#Advent of Code 2019: Day 14
from collections import defaultdict
from datetime import datetime
time_start = datetime.now()

def parse_data(lines):
    rules = defaultdict(list)
    for line in lines:
        left, right = line.split(" => ")
        amount, key = right.split(" ")
        rules[key].append(int(amount))
        for ingredient in left.split(", "):
            am, ingr = ingredient.split(" ")
            rules[key].append([ingr, int(am)])
    return rules

def solve_reactions(rules):
    def all_positive(stack):
        return not all(value >= 0 for value in stack.values())

    #negative = must be produced, positive = on stack for further use/remains from other reactions
    stack = dict({x: 0 for x in rules.keys()})
    stack["FUEL"] = -1
    stack["ORE"] = 0

    while all_positive(stack):
        for ingred, amount in stack.items():
            if amount >= 0:
                continue
            multipler, *new_products = rules[ingred]
            stack[ingred] += multipler
            for product in new_products:
                ing, am = product
                if ing == "ORE": #ORE can`t be negative - "all_positive" function would fail
                    stack[ing] += am
                else:
                    stack[ing] -= am
    return stack["ORE"]

#MAIN

"""file_names = "test1.txt,test2.txt,test3.txt,test4.txt,test5.txt".split(",")
results = list(map(int, "31,165,13312,180697,2210736".split(",")))

for name, expected_result in zip(file_names,results):
    with open(name) as file:
        lines = file.read().splitlines()

    rules = parse_data(lines)

    ore_count = solve_reactions(rules)

    print(f"Result for {name}: {ore_count}")

    assert ore_count == expected_result, f"Failed for {name}. Expected {expected_result}, got {ore_count}"
print("All tests correct \n")"""

with open("data.txt") as file:
    lines = file.read().splitlines()

rules = parse_data(lines)

ore_count = solve_reactions(rules)
print("Part 1:", ore_count)
print(datetime.now() - time_start)