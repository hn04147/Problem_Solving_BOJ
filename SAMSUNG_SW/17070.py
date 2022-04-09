import sys
from pprint import pprint
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
pipes = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]  #[가로, 대각선, 세로]
pipes[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if graph[i][j] == 0:
            if i == 0:
                pipes[i][j][0] = pipes[i][j-1][0]
            elif i > 0:
                if graph[i-1][j] == 0 and graph[i-1][j-1] == 0 and graph[i][j-1] == 0:
                    pipes[i][j][1] = pipes[i-1][j-1][0] + pipes[i-1][j-1][1] + pipes[i-1][j-1][2]
                pipes[i][j][0] = pipes[i][j-1][0] + pipes[i][j-1][1]
                pipes[i][j][2] = pipes[i-1][j][1] + pipes[i-1][j][2]

print(sum(pipes[-1][-1]))