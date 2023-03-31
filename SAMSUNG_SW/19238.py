import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m, oil = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
x, y = x - 1, y - 1
customers = [list(map(int, input().split())) for _ in range(m)]


for start_x, start_y, end_x, end_y in customers:
    graph[start_x-1][start_y-1] = (end_x-1, end_y-1)

def find_customer(x, y, graph):
    dq = deque([])
    dist = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    candidates = []

    if graph[x][y] != 0 and graph[x][y] != 1:
        return (x, y), 0

    dq.append((x, y))
    keep_going = True

    while dq:
        if keep_going:
            dist += 1
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == False:
                        if graph[nx][ny] == 0:
                            if keep_going:
                                visited[nx][ny] = True
                                dq.append((nx, ny))
                        elif graph[nx][ny] != 1:
                            if keep_going:
                                keep_going = False
                            candidates.append((nx, ny))
        if not keep_going:
            break

    candidates = sorted(candidates, key = lambda x : (x[0], x[1]))

    if not candidates:
        return (-1, -1), -1
    else:
        return candidates[0], dist


def find_destination(x, y, graph, oil):
    dq = deque([])
    dest_x, dest_y = graph[x][y]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dist = 0
    visited = [[False for _ in range(n)] for _ in range(n)]

    dq.append((x, y))

    while dq:
        dist += 1
        if dist > oil:
            break
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx == dest_x and ny == dest_y:
                    return dist
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] != 1:
                        if visited[nx][ny] == False:
                            visited[nx][ny] = True
                            dq.append((nx, ny))
    return -1

finish = True

for _ in range(m):
    c, dist = find_customer(x, y, graph)
    c_x, c_y = c

    if dist == -1:
        finish = False
        break

    oil -= dist

    if oil <= 0:
        finish = False
        break

    dist_to_dest = find_destination(c_x, c_y, graph, oil)

    if dist_to_dest == -1:
        finish = False
        break

    oil -= dist_to_dest

    if oil < 0:
        finish = False
        break

    oil += (dist_to_dest * 2)
    x, y = graph[c_x][c_y]
    graph[c_x][c_y] = 0

print(oil) if finish else print(-1)