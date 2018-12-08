import fileinput

data = ""
for line in fileinput.input():
    data = line

one = 0
two = 0
while one < len(data) - 1:
    two = one + 1
    if data[one] == data[two].swapcase():
        data = data[:one] + data[two + 1:]
        if one <= 0:
            one = 0
        else:
            one -= 1
    else:
        one += 1

print(len(data))
