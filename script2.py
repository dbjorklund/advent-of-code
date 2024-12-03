import re

with open('input.txt', 'r') as file:
    sigma = 0
    state = True
    for line in file:
        matches = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)
        for match in matches:
            if match == "don't()":
                state = False
                continue
            if match == "do()":
                state = True
                continue
            if state:
                x, y = match.split("mul")[-1].split('(')[-1].split(')')[0].split(',')
                sigma += int(x) * int(y)
    print(sigma)