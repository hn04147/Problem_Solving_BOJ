import sys
input = sys.stdin.readline

T = int(input())
arr = sorted([list(map(int, input().strip().split())) for _ in range(T)], key = lambda x : (x[1], x[0]))

cnt = 0
pos = 0

for i in arr:
  if i[0] >= pos:
    cnt += 1
    pos = i[1]

print(cnt)