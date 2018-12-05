import fileinput

sum = 0
results = set()
found = False

while not found:
    for line in fileinput.input():
        sum += int(line)
        if sum not in results:
            results.add(sum)
        else:
            found = True
            break

print(sum)
