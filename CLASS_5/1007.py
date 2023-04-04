import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]

    