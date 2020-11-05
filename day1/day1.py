import os
import copy

direction_map = {'R': {'N': 'E',
                       'E': 'S',
                       'S': 'W',
                       'W': 'N'},
                 'L': {'N': 'W',
                       'W': 'S',
                       'S': 'E',
                       'E': 'N'}}
position = [0, 0]
direction = 'N'
twice_visited = False
old_positions = []
with open('./day1/input.txt') as f:
    input = f.read().strip('\n').split(', ')
for step in input:
    direction = direction_map[step[:1]][direction]
    steps = step[1:]
    for _ in range(int(steps)):
        if direction == 'N':
            position[1] += 1
        if direction == 'S':
            position[1] -= 1
        if direction == 'E':
            position[0] += 1
        if direction == 'W':
            position[0] -= 1
        if position in old_positions and not twice_visited:
            twice_visited = True
            print(
                f'twice visited distance {abs(position[0]) + abs(position[1])}')
        old_positions.append(copy.deepcopy(position))
print(f'final distance {sum(position)}')
