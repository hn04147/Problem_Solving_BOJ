import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
steps = [list(map(int, input().rstrip().split())) for _ in range(M)]

ans = 0

# 회오리 도는 방향
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 마법 시전 방향
ddx = [-1, 1, 0, 0]
ddy = [0, 0, -1, 1]

for step in steps:
    d, s = step
    x, y = N // 2, N // 2
    step = 1
    direction = 0
    queue = deque([])


# 얼음 파편 공격
    for i in range(1, s+1):
        graph[x+ddx[d-1]*i][y+ddy[d-1]*i] = 0

    while True:
        if x == 0 and y == 0:
            break
        for _ in range(2):
            for i in range(step):
                if x == 0 and y == 0:
                    break
                x, y = x + dx[direction], y + dy[direction]
                if graph[x][y] != 0:
                    queue.append(graph[x][y])
            direction = (direction + 1) % 4
        step += 1


# 구슬 폭발 멈출 때 까지
    while True:
        stack = deque([])
        exploded = 0
        while queue:
            q = queue.popleft()
            if not queue:
                stack.append(q)
                break
            if q != queue[0]:
                stack.append(q)
            elif q == queue[0]:
                count = 1
                while True:
                    if count >= len(queue) or queue[count] != q:
                        break
                    count += 1
                if count >= 3:
                    for _ in range(count):
                        exploded += queue.popleft()
                    exploded += q
                else:
                    stack.append(q)
                    for _ in range(count):
                        stack.append(queue.popleft())

        queue = stack
        ans += exploded

        # print('queue', queue)
        # print('exploded', exploded)

        if exploded == 0:
            break


# 구슬 변화하는 단계
    stack = deque([])
    while queue:
        q = queue.popleft()
        if not queue or q != queue[0]:
            stack.append(1)
            stack.append(q)
        elif q == queue[0]:
            count = 1
            while True:
                if count >= len(queue) or queue[count] != q:
                    break
                count += 1
            for _ in range(count):
                queue.popleft()
            stack.append(count+1)
            stack.append(q)


# 그래프 갱신
    step = 1
    direction = 0
    x, y = N // 2, N // 2
    graph = [[0 for _ in range(N)] for _ in range(N)]

    while True:
        if x == 0 and y == 0:
            break
        if not stack:
            break
        for _ in range(2):
            for i in range(step):
                if not stack:
                    break
                if x == 0 and y == 0:
                    break
                x, y = x + dx[direction], y + dy[direction]
                graph[x][y] = stack.popleft()
            direction = (direction + 1) % 4
        step += 1

print(ans)