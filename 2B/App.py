import fileinput

lines = []
common_letters = ""

for word in fileinput.input():
    lines.append(word.replace("\n", ""))

for first in range(len(lines)):
    for second in range(first + 1, len(lines)):
        dif = 0
        for letter in range(len(lines[first])):
            if lines[first][letter] != lines[second][letter]:
                dif += 1

        if dif == 1:
            for index, letter in enumerate(lines[first]):
                if lines[first][index] == lines[second][index]:
                    common_letters += letter

print(common_letters)
