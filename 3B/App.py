import fileinput
import numpy as np

matrix = np.zeros((1000, 1000), dtype=np.int64)
res_id: ""

for line in fileinput.input():
    edges = list(map(int, line.replace(" ", "").split("@")[1].split(":")[0].split(",")))
    size = list(map(int, line.replace(" ", "").split("@")[1].split(":")[1].split("x")))

    for hor in range(edges[0], edges[0] + size[0]):
        for vert in range(edges[1], edges[1] + size[1]):
            matrix[hor][vert] += 1

for line in fileinput.input():
    claim_id = line.replace(" ", "").split("@")[0]
    edges = list(map(int, line.replace(" ", "").split("@")[1].split(":")[0].split(",")))
    size = list(map(int, line.replace(" ", "").split("@")[1].split(":")[1].split("x")))
    is_zero = True

    for hor in range(edges[0], edges[0] + size[0]):
        for vert in range(edges[1], edges[1] + size[1]):
            if matrix[hor][vert] > 1:
                is_zero = False
            matrix[hor][vert] += 1

    if is_zero:
        res_id = claim_id

print(res_id)
