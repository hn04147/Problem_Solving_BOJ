'''
Input:
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

Output:
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''
import sys

n = int(input())
arr = []
for _ in range(n):
  a = sys.stdin.readline()
  if a not in arr:
    arr.append(a)

arr.sort()
arr.sort(key = len)

for a in arr:
  print(a, end = '')