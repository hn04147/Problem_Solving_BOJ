import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        num = graph[i][j]
        if num == 0:
            break
        if j+num < N:
            dp[i][j+num] += dp[i][j]
        if i+num < N:
            dp[i+num][j] += dp[i][j]


print(dp[-1][-1])