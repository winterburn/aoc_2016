"""Solutions for day 8 of 2016 AOC"""

display = [[False] * 50, [False] * 50, [False]
           * 50, [False] * 50, [False] * 50, [False] * 50]


def draw_screen():
    """Prints the current display buffer"""
    print('\n', flush=True)
    for row in display:
        for column in row:
            if column:
                print("#", end='')
            else:
                print(".", end='')
        print('\n')


def add_rect(x, y):
    """Adds a rectangle to top left corner"""
    for row in range(int(y)):
        for column in range(int(x)):
            display[row][column] = True


def rotate_row(row, times):
    """Rotate the row to the right number of times"""
    display[row] = display[row][-times:] + display[row][:-times]


def rotate_column(column, times):
    """Rotate the column down number of times"""
    temp = [row[column] for row in display]
    temp = temp[-times:] + temp[:-times]
    for idx, value in enumerate(temp):
        display[idx][column] = value


with open('./day8/input.txt') as f:
    data = f.readlines()
for line in data:
    splitted = line.split(' ')
    if splitted[0] == 'rect':
        add_rect(*splitted[1].split('x'))
    if splitted[1] == 'row':
        rotate_row(int(splitted[2].split('=')[1]), int(splitted[-1]))
    elif splitted[1] == 'column':
        rotate_column(int(splitted[2].split('=')[1]), int(splitted[-1]))
draw_screen()
count = 0
for row in display:
    for pixel in row:
        count += pixel
print(f'lit pixels {count}')
