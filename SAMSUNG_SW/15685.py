import sys
input = sys.stdin.readline

n = int(input().rstrip())
curves = []
for _ in range(n):
    x, y, d, g = map(int, input().rstrip().split())
    curves.append((x, y, d, g))

grid = [[0 for _ in range(101)] for _ in range(101)]
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for x, y, d, g in curves:
    curve = [(x, y)]
    curve.append((x + direction[d][0], y + direction[d][1]))

    for _ in range(g):
        last_x, last_y = curve[-1]

        for x_, y_ in curve[:-1][::-1]:
            curve.append((last_x - y_ + last_y, last_y + x_ - last_x))

    for x_, y_ in curve:
        grid[x_][y_] = 1

count = 0

for i in range(100):
    for j in range(100):
        if grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1] == 1:
            count += 1

print(count)