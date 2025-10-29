#Advent of Code 2019: Day 10
from math import atan2, pi, inf
from icecream import ic
from collections import defaultdict

def check_visible(space):
    angles = defaultdict(list)
    s_r, s_c = space
    for asteroid in asteroids:
        if asteroid == space: continue
        a_r, a_c = asteroid
        d_r = a_r - s_r
        d_c = a_c - s_c
        angle = atan2(d_r, d_c) + pi/2
        if angle > pi:
            angle = angle - 2*pi
        angles[angle].append(asteroid)
    return angles, len(angles)

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def to_be_vaporized(asteroids, center):
    nearest = inf
    vaporized = False
    for asteroid in asteroids:
        distance = manh_distance(asteroid, center)
        if distance < nearest:
            nearest = distance
            vaporized = asteroid
    return vaporized


#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

asteroids = set()
spaces = set()
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char != ".":
            asteroids.add((row, col))

max_count = 0
for asteroid in asteroids:
    angles, count = check_visible(asteroid)
    if count > max_count:
        max_count = count
        center = asteroid
        saved_angles = angles
print(f"Part 1: {max_count}")

result = 0
counter = 1
positive = sorted([angle for angle in saved_angles.keys() if angle >= 0])
negative = sorted([angle for angle in saved_angles.keys() if angle < 0])
while counter <= 300:
    for angle in positive:
        if len(saved_angles[angle]) == 0: continue
        vaporize = to_be_vaporized(saved_angles[angle], center)
        index = saved_angles[angle].index(vaporize)
        if counter == 200:
            result = vaporize
        counter += 1
    for angle in negative:
        if len(saved_angles[angle]) == 0: continue
        vaporize = to_be_vaporized(saved_angles[angle], center)
        index = saved_angles[angle].index(vaporize)
        saved_angles[angle].pop(index)
        if counter == 200:
            result = vaporize
        counter += 1

x, y = result
print(f"Part 2: 200th asteroid: {(y,x)}: result = {100*y + x}")
