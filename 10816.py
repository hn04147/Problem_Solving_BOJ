'''
Input:
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

Output:
3 0 0 1 2 0 0 2
'''

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())
nums = list(map(int, sys.stdin.readline().split()))

dict1 = dict()
for i in arr:
  if i in dict1:
    dict1[i] += 1
  else:
    dict1[i] = 1

for num in nums:
  if num in dict1:
    sys.stdout.write(str(dict1[num]) + ' ')
  else:
    sys.stdout.write('0 ')