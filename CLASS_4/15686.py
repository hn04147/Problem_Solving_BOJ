import sys
import math
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
chickens = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append((i, j))

def get_chicken_distance(arr):
    distance = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                min_distance = 10000
                for a in arr:
                    idx = abs(chickens[a][0] - i) + abs(chickens[a][1] - j)
                    if min_distance > idx:
                        min_distance = idx
                distance += min_distance
    return distance

result = 10000

for c in list(combinations([i for i in range(len(chickens))], M)):
    idx = get_chicken_distance(c)
    if idx < result:
        result = idx

print(result)