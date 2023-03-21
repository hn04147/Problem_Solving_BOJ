import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
A = []
nutrients = [[5 for _ in range(n)] for _ in range(n)]
trees = [[deque([]) for _ in range(n)] for _ in range(n)]
for _ in range(n):
    A.append(list(map(int, input().rstrip().split())))
for _ in range(m):
    x, y, z = map(int, input().rstrip().split())
    trees[x-1][y-1].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                tree_cnt = len(trees[i][j])
                nutrient = nutrients[i][j]
                for k in range(tree_cnt):
                    if nutrient >= trees[i][j][k]:
                        nutrient -= trees[i][j][k]
                        trees[i][j][k] += 1
                    else:
                        for l in range(tree_cnt - k):
                            x = trees[i][j].pop()
                            nutrient += x // 2
                        break
                nutrients[i][j] = nutrient

    # print('trees', trees)
    # print('nutrients', nutrients)

    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for tree in trees[i][j]:
                    if tree % 5 == 0:
                        for x, y in zip(dx, dy):
                            if 0 <= (x + i) < n and 0 <= (y + j) < n:
                                trees[x+i][y+j].appendleft(1)
            nutrients[i][j] += A[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans)