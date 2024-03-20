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

def solve_reactions(rules, fuel):
    def all_positive(stack):
        return not all(value >= 0 for value in stack.values())

    #negative = must be produced, positive = on stack for further use/remains from other reactions
    stack = dict({x: 0 for x in rules.keys()})
    stack["FUEL"] = - fuel
    stack["ORE"] = 0

    while all_positive(stack):
        for ingred, amount in stack.items():
            if amount >= 0:
                continue
            multipler, *new_products = rules[ingred]
            help = max(1, (-1 *amount) // multipler) #if help == 0, help = 1
            stack[ingred] += (multipler * help )
            for product in new_products:
                ing, am = product
                if ing == "ORE": #ORE can`t be negative - "all_positive" function would fail
                    stack[ing] += am * help
                else:
                    stack[ing] -= am * help
    return stack["ORE"]

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
rules = parse_data(lines)

#Part 1
ore_count = solve_reactions(rules, 1)
print("Part 1:", ore_count)

#Part 2
start = 0
end = 5_000_000
huge_number = 1000000000000

#binary bisection
#total amount of ore needed for X fuel production must be smaller than huge_number
while start + 1 != end:
    mid = (end  + start) // 2
    ore_count = huge_number - solve_reactions(rules, mid)
    if ore_count > 0:
        start = mid
    else:
        end = mid

print("Part 2:", start)