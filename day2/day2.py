location = [0, 2]
keymap = [[1],
          [2, 3, 4],
          [5, 6, 7, 8, 9],
          ['A', 'B', 'C'],
          ['D']]

keycode = []

with open('./day2/input.txt') as f:
    for line in f.readlines():
        input = list(line.strip('\n'))
        for direction in input:
            if direction == 'U' and location[1] > 0:
                if location[1] == 1 and location[0] not in [0, 2]:
                    location[1] -= 1
                    location[0] -= 1
                elif location[1] == 2 and location[0] not in [0, 4]:
                    location[1] -= 1
                    location[0] -= 1
                elif location[1] > 2:
                    location[1] -= 1
                    location[0] += 1
            elif direction == 'D' and location[1] < 4:
                if location[1] == 2 and location[0] not in [0, 4]:
                    location[1] += 1
                    location[0] -= 1
                elif location[1] == 3 and location[0] not in [0, 2]:
                    location[1] += 1
                    location[0] -= 1
                elif location[1] < 2:
                    location[1] += 1
                    location[0] += 1
            elif direction == 'L' and location[0] > 0:
                location[0] -= 1
            elif direction == 'R' and location[0] < len(keymap[location[1]])-1:
                location[0] += 1
            print(direction, location)

        print(location)
        keycode.append(keymap[location[1]][location[0]])
print(keycode)
