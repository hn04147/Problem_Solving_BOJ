import sys
input = sys.stdin.readline

h, w = map(int, input().split())

mat = [[] for i in range(h)]
dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]

for i in range(h):
    ss = input().strip()
    for s in ss:
        mat[i].append(int(s))

def bfs(y, x):
    q = [[y, x]]
    while q:
        now = q.pop(0)
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if 0 <= nx < w and 0 <= ny < h and mat[ny][nx] == 1:
                mat[ny][nx] = mat[now[0]][now[1]] + 1
                q.append([ny, nx])

bfs(0, 0)
print(mat[-1][-1])