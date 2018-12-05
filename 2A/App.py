import fileinput

count_two = 0
count_three = 0

for word in fileinput.input():
    has_two = False
    has_three = False
    letters = {}

    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter in letters:
        if letters[letter] == 2 and not has_two:
            count_two += 1
            has_two = True
        elif letters[letter] == 3 and not has_three:
            count_three += 1
            has_three = True

print(count_two * count_three)
