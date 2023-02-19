#Advent of Code 2019: Day2
from intcode import intcode_computer

def part1(numbers):
    numbers[1] = 12
    numbers[2] = 2
    result = intcode_computer(numbers)
    return result[0]

def part2(numbers, noun, verb):
    numbers[1] = noun
    numbers[2] = verb
    result = intcode_computer(numbers)
    return result[0]

with open("02data.txt") as file:
    numbers = list(map(int,file.read().split(",")))

#Task1
print("Task 1:",part1(numbers[:]))

#Task2
for noun in range(100):
    for verb in range(100):
        if part2(numbers[:], noun, verb) == 19690720:
            result = noun*100 + verb
            break
print("Task 2:", result)
