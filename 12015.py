import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
stack = [0]

for a in arr:
  if stack[-1] < a:
    stack.append(a)
  else:
    stack[bisect_left(stack, a)] = a

print(len(stack) - 1)