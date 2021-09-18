'''
Input:
4 11
802
743
457
539

Output:
200
'''

import sys

k, n = map(int, sys.stdin.readline().split())
lines = []
for _ in range(k):
  lines.append(int(input()))

start, end = 1, max(lines)

while start <= end:
  mid = (start + end) // 2
  num = 0
  for line in lines:
    num += line // mid
  
  if num >= n:
    start = mid + 1
  else:
    end = mid - 1

print(end)