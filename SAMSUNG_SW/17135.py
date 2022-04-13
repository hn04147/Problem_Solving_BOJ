import sys
from pprint import pprint
from itertools import combinations
input = sys.stdin.readline

N, M, D = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
graph_copied = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        graph_copied[i][j] = graph[i][j]

ans = 0

def move_down():
    for i in range(N-1, 0, -1):
        graph[i] = graph[i-1]
    graph[0] = [0 for _ in range(M)]

for archers in list(combinations(range(M), 3)):
    max_removed = 0

    for i in range(N):
        for j in range(M):
            graph[i][j] = graph_copied[i][j]

    for _ in range(N):
        removed_archers = set()

        for y in archers:
            idx = 0
            is_finished = False
            while True:
                if idx >= D:
                    break
                for i in range(idx):
                    nx, ny = N-1-i, y-idx+i
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                        is_finished = True
                        removed_archers.add((nx, ny))
                        break
                if is_finished:
                    break

                nx = N-1-idx
                if 0 <= nx < N and graph[nx][y] == 1:
                    is_finished = True
                    removed_archers.add((nx, y))
                    break
                if is_finished:
                    break

                for i in range(idx):
                    nx, ny = N-idx+i, y+1+i
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                        is_finished = True
                        removed_archers.add((nx, ny))
                        break
                if is_finished:
                    break

                idx += 1

        max_removed += len(removed_archers)
        for x, y in removed_archers:
            graph[x][y] = 0

        move_down()

    ans = max(ans, max_removed)

print(ans)