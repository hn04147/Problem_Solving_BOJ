'''
Input:
5
5
4
3
2
1

Output:
1
2
3
4
5
'''

import sys

n = int(input())
l = []
for i in range(n):
  l.append(int(sys.stdin.readline()))
for i in sorted(l):
  sys.stdout.write(str(i)+'\n')