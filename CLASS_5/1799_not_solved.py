import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
ans = 0

def check_available(x, y):
    directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        a, b = x, y
        while 0 <= a+dx < n and 0 <= b+dy < n:
            a += dx
            b += dy
            if board[a][b] == -1:
                return False
    return True

def dfs(loc, cnt):
    global ans

    x = loc // n
    y = loc % n

    if loc == n*n-1:
        if board[x][y] == 1:
            if check_available(x, y):
                cnt += 1
        if ans < cnt:
            ans = cnt
            # print(*board, sep='\n')
        return

    elif board[x][y] == 1:
        if check_available(x, y):
            board[x][y] = -1
            dfs(loc+1, cnt+1)
            board[x][y] = 1

    dfs(loc+1, cnt)

    return

dfs(0, 0)

print(ans)