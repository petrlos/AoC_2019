#Advent of Code 2019: Day 22

import re
def deal_into_new_stack(deck):
    return list(reversed(deck))

def cut_N_cards(deck, n): #simplified
    return deck[n:] + deck[:n]

def deal_with_increment(deck, increment):
    size = len(deck)
    new_deck = [0] * size
    index = 0
    for card in deck:
        new_deck[index] = card
        index = (index + increment) % size  # wrap around if necessary
    return new_deck

def run_instructions(file_name, size):
    regNum = re.compile(r"-?\d+")
    with open(file_name) as file:
        lines = file.read().splitlines()
    deck = list(range(size))
    for line in lines:
        if "increment" in line:
            n = int(regNum.search(line).group())
            deck = deal_with_increment(deck, n)
        elif "cut" in line:
            n = int(regNum.search(line).group())
            deck = cut_N_cards(deck, n)
        elif "new" in line:
            deck = deal_into_new_stack(deck)
    return deck

#MAIN:

new_deck = run_instructions("data.txt", 10007)
print("Task 1:", new_deck.index(2019))
