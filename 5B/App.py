import sys
import string
import fileinput

data = ""
for line in fileinput.input():
    data = line

total_length = sys.maxsize

for letter in string.ascii_lowercase:
    one = 0
    two = 0
    temp = data.replace(letter, "")
    temp = temp.replace(letter.upper(), "")
    while one < len(temp) - 1:
        two = one + 1
        if temp[one] == temp[two].swapcase():
            temp = temp[:one] + temp[two + 1:]
            if one <= 0:
                one = 0
            else:
                one -= 1
        else:
            one += 1
    if len(temp) < total_length:
        total_length = len(temp)

print(total_length)
