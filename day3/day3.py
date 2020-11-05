def possible_triangle(sides):
    comp1 = float(sides[0]) + float(sides[1]) > float(sides[2])
    comp2 = float(sides[0]) + float(sides[2]) > float(sides[1])
    comp3 = float(sides[2]) + float(sides[1]) > float(sides[0])
    return all([comp1, comp2, comp3])


with open('./day3/input.txt') as f:
    lines = f.readlines()
count = 0
triangles = [[], [], []]
for idx, line in enumerate(lines):
    x, y, z = line.split()
    idx += 1
    triangles[0].append(x)
    triangles[1].append(y)
    triangles[2].append(z)
    if not idx % 3:
        print(triangles)
        for triangle in triangles:
            count += possible_triangle(triangle)
        triangles = [[], [], []]

print(count)
