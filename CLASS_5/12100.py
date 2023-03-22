import sys
from collections import deque
from copy import deepcopy
from pprint import pprint
input = sys.stdin.readline

n = int(input().rstrip())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))

def step(q):
    return_q = deque([])

    while q:
        num = q.popleft()
        if len(q) > 0 and num == q[0]:
            return_q.append(num + q.popleft())
        else:
            return_q.append(num)

    return return_q

def move(b, direction): # 1: up, 2: down, 3: left, 4: right
    q = deque([])

    if direction == 1:
        for i in range(n):
            for j in range(n):
                if b[j][i] != 0:
                    q.append(b[j][i])

            q = step(q)

            len_q = len(q)
            for j in range(len_q):
                b[j][i] = q.popleft()
            for j in range(len_q, n):
                b[j][i] = 0

    elif direction == 2:
        for i in range(n):
            for j in range(n-1, -1, -1):
                if b[j][i] != 0:
                    q.append(b[j][i])

            q = step(q)

            len_q = len(q)
            for j in range(n-1, n-len_q-1, -1):
                b[j][i] = q.popleft()
            for j in range(n-len_q-1, -1, -1):
                b[j][i] = 0

    elif direction == 3:
        for i in range(n):
            for j in range(n):
                if b[i][j] != 0:
                    q.append(b[i][j])
            
            q = step(q)

            len_q = len(q)
            for j in range(len_q):
                b[i][j] = q.popleft()
            for j in range(len_q, n):
                b[i][j] = 0

    elif direction == 4:
        for i in range(n):
            for j in range(n-1, -1, -1):
                if b[i][j] != 0:
                    q.append(b[i][j])

            q = step(q)

            len_q = len(q)
            for j in range(n-1, n-len_q-1, -1):
                b[i][j] = q.popleft()
            for j in range(n-len_q-1, -1, -1):
                b[i][j] = 0

    return b


directions = [1, 2, 3, 4]
ans = 0

def dfs(board, step_num):
    global ans

    if step_num == 5:
        for direction in directions:
            b = move(deepcopy(board), direction)
            if ans < max([max(i) for i in b]):
                ans = max([max(i) for i in b])
        return

    for direction in directions:
        b = move(deepcopy(board), direction)
        dfs(b, step_num+1)

    return

dfs(board, 1)

print(ans)