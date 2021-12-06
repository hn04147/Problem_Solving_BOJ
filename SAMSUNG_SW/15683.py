import sys
input = sys.stdin.readline

n, m = int(input().rstrip().split())
room = [list(map(int, input().rstrip().split())) for _ in range(n)]
