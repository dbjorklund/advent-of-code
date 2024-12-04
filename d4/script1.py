import numpy as np

def check_right(m) -> int:
    count = 0
    start_indices = np.where(m == 'X')
    for (y, x) in zip(start_indices[0], start_indices[1]):
        if x > m.shape[1] - 4:
            continue
        if m[y][x+1] == 'M' and m[y][x+2] == 'A' and m[y][x+3] == 'S':
            count += 1
    return count

def check_diag(m) -> int:
    count = 0
    start_indices = np.where(m == 'X')
    for (y, x) in zip(start_indices[0], start_indices[1]):
        if y > m.shape[0] - 4 or x > m.shape[1] - 4:
            continue
        if m[y+1][x+1] == 'M' and m[y+2][x+2] == 'A' and m[y+3][x+3] == 'S':
            count += 1
    return count

first = True
matrix = None
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        if first:
            matrix = np.array([c for c in line])
            first = False
            continue
        matrix = np.vstack([matrix, [c for c in line]])
count = 0
for _ in range(4):
    count += check_right(matrix)
    count += check_diag(matrix)
    matrix = np.rot90(matrix)
print(f"Res: {count}")
    