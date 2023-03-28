import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

ans = 0

def check(r):
    global n, l, ans
    ramp = [False] * n
    idx = 0

    while idx < n-1:
        if r[idx] == r[idx+1]:
            idx += 1
        elif r[idx] == r[idx+1] + 1:
            if idx + l >= n:
                return False
            for i in range(idx+1, idx+1+l):
                if r[i] != r[idx] - 1:
                    return False
            for i in range(idx+1, idx+1+l):
                ramp[i] = True
            idx += l
        elif r[idx] == r[idx+1] - 1:
            if idx - l + 1 < 0:
                return False
            for i in range(idx, idx-l, -1):
                if r[i] != r[idx+1] - 1 or ramp[i] == True:
                    return False
            for i in range(idx, idx-l, -1):
                ramp[i] = True
            idx += 1
        else:
            return False

    return True


for i in range(n):
    if check([graph[i][j] for j in range(n)]):
        ans += 1
    if check([graph[j][i] for j in range(n)]):
        ans += 1

print(ans)