import fileinput
import numpy as np

matrix = np.zeros((1000, 1000), dtype=np.int64)
count = 0

for line in fileinput.input():
    edges = list(map(int, line.replace(" ", "").split("@")[1].split(":")[0].split(",")))
    size = list(map(int, line.replace(" ", "").split("@")[1].split(":")[1].split("x")))

    for hor in range(edges[0], edges[0] + size[0]):
        for vert in range(edges[1], edges[1] + size[1]):
            matrix[hor][vert] += 1

for x in range(1000):
    for y in range(1000):
        if matrix[x][y] > 1:
            count += 1

print(count)
