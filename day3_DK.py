# http://adventofcode.com/2016/day/3

from itertools import combinations
from pandas import read_fwf

# all combinations of 2 sides of a triangle
tri = [list(n) for n in combinations(range(3), 2)]
for n in range(3):
    tri[n].append(list(reversed(range(3)))[n])

def check_tri(sides):
    """checks whether the sum of any two sides must be larger than the remaining side"""
    while True:
        for n in tri:
            if not(sides[n[0]] + sides[n[1]] > sides[n[2]]):
                return False
        else:
            # loop fell through without finding violation, so sides is a triangle
            return True

data = read_fwf('day3_input_DK.txt', header=None, widths=[5,5,5])

possible_triangles = 0
for row in data.iterrows():
    if check_tri(row[1]):
        possible_triangles += 1

print('Number of possible triangles: {}'.format(possible_triangles))

# triangles defined vertically
pos_tri = 0
for col in data.columns:
    for t in range(0, len(data), 3):
        if check_tri(list(data[col][t:t+3])):
            pos_tri += 1

print('Number of possible triangles: {}'.format(pos_tri))
