import sys

n = int(input())
for _ in range(n):
  h, w, t = list(map(int,sys.stdin.readline().split()))
  total = h * w
  room_num = str((t - 1) % h + 1) + (str((t - 1) // h + 1) if len(str((t - 1) // h + 1)) > 1 else ('0' + str((t - 1) // h + 1)))
  print(room_num)