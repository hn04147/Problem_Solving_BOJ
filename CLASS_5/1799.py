import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
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
    if loc == (n-1, n-1):
        ans = cnt if cnt > ans else ans
        return

    if board[loc[0]][loc[1]] == 0:
        dfs(loc[])