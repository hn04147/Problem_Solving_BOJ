'''
Input:
5
3 4
1 1
1 -1
2 2
3 3

Output:
1 -1
1 1
2 2
3 3
3 4
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  a, b = map(int, input().split())
  arr.append((a, b))

arr.sort(key = lambda x : x[1])
arr.sort(key = lambda x : x[0])

for i in arr:
  sys.stdout.write(str(i[0]) + ' ' + str(i[1]) + '\n')