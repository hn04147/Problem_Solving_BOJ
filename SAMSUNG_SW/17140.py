import sys
from pprint import pprint
from collections import Counter
input = lambda : sys.stdin.readline().rstrip()

r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]

ans = 0

while True:
    if r-1 < len(matrix) and c-1 < len(matrix[0]):
        if matrix[r-1][c-1] == k:
            break

    if ans >= 100:
        ans = -1
        break

    cal_type = 'R'
    tmp_matrix = []
    new_matrix = []

    if len(matrix) >= len(matrix[0]): # R
        tmp_matrix = matrix
    else: # C
        cal_type = 'C'
        tmp_matrix = list(map(list, zip(*matrix)))

    for m in tmp_matrix:
        count = list(sorted(Counter(m).items()))
        count = sorted(count, key = lambda x : (x[1], x[0]))
        n = []
        for a, b in count:
            if a != 0:
                n.append(a)
                n.append(b)
        new_matrix.append(n)

    max_length = max([len(m) for m in new_matrix])

    for i, m in enumerate(new_matrix):
        if len(m) < max_length:
            for _ in range(max_length - len(m)):
                new_matrix[i].append(0)

    if cal_type == 'C':
        matrix = list(map(list, zip(*new_matrix)))
    else:
        matrix = new_matrix

    ans += 1

print(ans)