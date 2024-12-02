import numpy as np
import copy


def incrementingOnly(line):
    failed_index = -1
    failed = False
    for i in range(len(line) - 1):
        if int(line[i]) < int(line[i+1]) and np.abs(int(line[i]) - int(line[i+1])) <= 3:
            continue
        else:
            failed_index = i
            failed = True
            break
    if failed:
        # Try first index to be removed
        first_line = copy.deepcopy(line)
        del first_line[failed_index]
        for k in range(len(first_line) - 1):
            if int(first_line[k]) < int(first_line[k+1]) and np.abs(int(first_line[k]) - int(first_line[k+1])) <= 3:
                if k == len(first_line) - 2:
                    return True
                continue
            else:
                break
        # Try second index to be removed
        second_line = copy.deepcopy(line)
        if failed_index + 1 < len(line) - 1:
            del second_line[failed_index + 1]
            for k in range(len(second_line) - 1):
                if int(second_line[k]) < int(second_line[k+1]) and np.abs(int(second_line[k]) - int(second_line[k+1])) <= 3:
                    continue
                else:
                    return False
    return True

def decreasingOnly(line):
    failed_index = -1
    failed = False
    for i in range(len(line) - 1):
        if int(line[i]) > int(line[i+1]) and np.abs(int(line[i]) - int(line[i+1])) <= 3:
            continue
        else:
            failed_index = i
            failed = True
            break
    if failed:
        # Try first index to be removed
        first_line = copy.deepcopy(line)
        del first_line[failed_index]
        for k in range(len(first_line) - 1):
            if int(first_line[k]) > int(first_line[k+1]) and np.abs(int(first_line[k]) - int(first_line[k+1])) <= 3:
                if k == len(first_line) - 2:
                    return True
                continue
            else:
                break
        # Try second index to be removed
        second_line = copy.deepcopy(line)
        if failed_index + 1 < len(line) - 1:
            del second_line[failed_index + 1]
            for k in range(len(second_line) - 1):
                if int(second_line[k]) > int(second_line[k+1]) and np.abs(int(second_line[k]) - int(second_line[k+1])) <= 3:
                    continue
                else:
                    return False
    return True

with open('input.txt', 'r') as file:
    count = 0
    for line in file:
        line = line.split('\n')
        line = line[0].split(" ")
        incrementing = incrementingOnly(copy.deepcopy(line))
        if not incrementing:
            decrementing = decreasingOnly(copy.deepcopy(line))
        if incrementing or decrementing:
            count += 1
    print(count)