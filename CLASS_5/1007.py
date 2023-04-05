import sys
import math
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n = int(input())
    ans = 10e9
    points = [list(map(int, input().split())) for _ in range(n)]

    for l_points in list(combinations([i for i in range(n)], n//2)):
        l_points = list(l_points)

        l_points_x, l_points_y = 0, 0
        r_points_x, r_points_y = 0, 0

        for p in range(n):
            if p in l_points:
                l_points_x += points[p][0]
                l_points_y += points[p][1]
            else:
                r_points_x += points[p][0]
                r_points_y += points[p][1]

        distance = math.sqrt((l_points_x - r_points_x) ** 2 + (l_points_y - r_points_y) ** 2)
        ans = distance if distance < ans else ans

    print(ans)
