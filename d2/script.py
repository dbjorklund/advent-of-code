import os
import numpy as np


def incrementingOnly(line):
    unsafeUsed = False
    for i in range(len(line) - 1):
        if int(line[i]) < int(line[i+1]) and np.abs(int(line[i]) - int(line[i+1])) <= 3:
            continue
        else:
            if unsafeUsed:
                return False
            else:
                if i+1 == len(line) - 1:
                    continue
                line[i] = line[i+1]
                unsafeUsed = True
    return True

def decreasingOnly(line):
    unsafeUsed = False
    for i in range(len(line) - 1):
        if int(line[i]) > int(line[i+1]) and np.abs(int(line[i]) - int(line[i+1])) <= 3:
            continue
        else:
            if unsafeUsed:
                return False
            else:
                if i+1 == len(line) - 1:
                    continue
                line[i] = line[i+1]
                unsafeUsed = True
    return True

with open('input.txt', 'r') as file:
    count = 0
    for line in file:
        line = line.split('\n')
        line = line[0].split(" ")
        incrementing = incrementingOnly(line)
        decrementing = decreasingOnly(line)
        if incrementing or decrementing:
            count += 1
    print(count)


# 