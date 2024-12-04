import numpy as np

def check_Xv(m) -> int:
    count = 0
    start_indices = np.where(m == 'A')
    for (y, x) in zip(start_indices[0], start_indices[1]):
        if x > m.shape[1] - 2 or x < 1 or y > m.shape[0] - 2 or y < 1:
            continue
        if m[y-1][x-1] == 'M' and m[y+1][x+1] == 'S' and m[y-1][x+1] == 'M' and m[y+1][x-1] == 'S':
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
    count += check_Xv(matrix)
    matrix = np.rot90(matrix)
print(f"Res: {count}")