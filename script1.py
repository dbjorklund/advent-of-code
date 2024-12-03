import re

with open('input.txt', 'r') as file:
    regex = r"mul\(\d+,\d+\)"
    sigma = 0
    for line in file:
        matches = re.findall(regex, line)
        for match in matches:
            x,y = match.split('(')[1].split(')')[0].split(',')
            sigma += int(x) * int(y)
    print(sigma)