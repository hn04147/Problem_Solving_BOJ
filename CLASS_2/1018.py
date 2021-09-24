'''
Example 1)
Input:
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

Output:
1

Example 2)
Input:
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

Output:
12
'''

import sys

arr = []
m, n = map(int, sys.stdin.readline().split())
for _ in range(m):
  arr.append(input())

minimum = 64

for i in range(m - 7):
  for j in range(n - 7):
    count = 0

    for x in range(i, i + 8):
      for y in range(j, j + 8):
        if (x + y) % 2 == 0:
          if (arr[x][y] != 'W'):
            count += 1
        else:
          if (arr[x][y] != 'B'):
            count += 1
    
    if min(count, 64 - count) < minimum:
      minimum = min(count, 64 - count)

print(minimum)