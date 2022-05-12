import sys
from collections import deque
input = sys.stdin.readline

graph = [i for i in range(101)]
visited = [False for _ in range(101)]
visited[1] = True
q = deque([1])
step = 0
found = False

N, M = map(int, input().rstrip().split())
for _ in range(N+M):
    x, y = map(int, input().rstrip().split())
    graph[x] = y

while q and not found:
    step += 1
    for _ in range(len(q)):
        pos = q.popleft()
        for i in range(1, 7):
            next_pos = pos + i
            if next_pos <= 100:
                next_pos = graph[next_pos]
                if visited[next_pos] == False:
                    visited[next_pos] = True
                    q.append(next_pos)
                    if next_pos == 100:
                        print(step)
                        found = True
                        break
