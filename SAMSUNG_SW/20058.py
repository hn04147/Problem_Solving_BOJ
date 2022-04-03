import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(2**N)]
L = list(map(int, input().rstrip().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for q in range(Q):
    l = L[q]
    n = 2 ** l
    after_magic = [[0 for _ in range(2**N)] for _ in range(2**N)]

    for i in range(0, 2**N, n):
        for j in range(0, 2**N, n):
            for x in range(n):
                for y in range(n):
                    after_magic[i+x][j+y] = graph[i+(n-y-1)][j+x]

    for i in range(2**N):
        for j in range(2**N):
            graph[i][j] = after_magic[i][j]

    for i in range(2**N):
        for j in range(2**N):
            idx = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < 2**N and 0 <= ny < 2**N:
                    if after_magic[nx][ny] > 0:
                        idx += 1
            if idx < 3:
                graph[i][j] = max(graph[i][j] - 1, 0)

    after_magic = []

print(sum([sum(i) for i in graph]))

ans = 0
visited = [[False for _ in range(2**N)] for _ in range(2**N)]
queue = deque([])

for i in range(2**N):
    for j in range(2**N):
        if graph[i][j] == 0:
            visited[i][j] = True
        elif graph[i][j] > 0 and visited[i][j] == False:
            num = 0
            queue.append([i, j])
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                num += 1
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < 2**N and 0 <= ny < 2**N:
                        if graph[nx][ny] > 0 and visited[nx][ny] == False:
                            queue.append([nx, ny])
                            visited[nx][ny] = True
            ans = max(ans, num)

print(ans)