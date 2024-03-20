#Advent of Code 2019: Day 14
from icecream import ic
from collections import deque, defaultdict

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

def clean_up(needed):
    needed_dict = defaultdict(int)
    result = deque()
    for item in needed:
        ingred, count = item
        needed_dict[ingred] += count
    for key, value in needed_dict.items():
        result.append([key, value])
    return result

def solve_reactions(rules):
    needed = deque([["FUEL", 1]])
    stack = dict({x: 0 for x in rules.keys()})

    ore_count = 0
    while needed:
        ingr, quan_needed = needed.popleft()
        if quan_needed == 0:
            continue
        if ingr == "ORE":
            ore_count += quan_needed
            continue
        multipler = quan_needed // rules[ingr][0]
        if multipler == 0:
            multipler = 1
        if quan_needed % rules[ingr][0] > 0:
            multipler += 1
        stack[ingr] += rules[ingr][0] * multipler - quan_needed
        for item in rules[ingr][1:]:
            ingr_needed, quantity = item
            needed.append([ingr_needed, quantity * multipler])
        for index, item in enumerate(needed):
            ingr, count = item
            if ingr == "ORE":
                continue
            used_items = min(count, stack[ingr])
            needed[index][1] = max(0, count - stack[ingr])
            stack[ingr] = max(0, stack[ingr] - used_items)
        needed = clean_up(needed)
    return ore_count

#MAIN

file_names = "test1.txt,test2.txt,test3.txt,test4.txt,test5.txt".split(",")
results = map(int, "31,165,13312,180697,2210736".split(","))

for name, expected_result in zip(file_names,results):
    with open(name) as file:
        lines = file.read().splitlines()

    rules = parse_data(lines)

    ore_count = solve_reactions(rules)

    print(f"Result for {name}: {ore_count}")

    assert ore_count == expected_result, f"Failed for {name}. Expected {expected_result}, got {ore_count}"
