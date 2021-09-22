'''
Input:
3
21 Junkyu
21 Dohyun
20 Sunyoung

Output:
20 Sunyoung
21 Junkyu
21 Dohyun
'''

import sys

n = int(input())
arr = []

for i in range(n):
  age, name = map(str, sys.stdin.readline().split())
  age = int(age)
  arr.append((age, name))

arr.sort(key = lambda x : x[0])

for i in arr:
  sys.stdout.write(str(i[0]) + ' ' + i[1] + '\n')