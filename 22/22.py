#Advent of Code 2019: Day 22
#TODO: test working, data not

import re
def dealIntoNewStack(deck):
    return list(reversed(deck))

def cutNCards(deck, n):
    if n > 0:
        cut = deck[0:n]
        rest = deck[n:]
        return rest + cut
    else:
        cut = deck[n:]
        rest = deck[:n]
        return cut + rest

def dealWithIncrement(deck, n):
    oldDeck = {}
    newDeck = {}
    for index, card in enumerate(deck):
        oldDeck.setdefault(index, card)
        newDeck.setdefault(index, None)
    currentPosition = 0
    for i in range(len(deck)):
        newDeck[currentPosition] = oldDeck[i]
        currentPosition = (currentPosition + n) % len(deck)
    result = []
    for i in range(len(deck)):
        result.append(newDeck[i])
    return result

#MAIN:
regNum = re.compile(r"-?\d")

with open("data.txt") as file:
    lines = file.read().splitlines()

deck = list(range(10007))


for line in lines:
    if "increment" in line:
        n = int(regNum.search(line).group())
        deck = dealWithIncrement(deck, n)
    if "cut" in line:
        n = int(regNum.search(line).group())
        deck = cutNCards(deck, n)
    if "new" in line:
        deck = dealIntoNewStack(deck)

print(deck.index(2019))

print(deck[8971])