# import sys
# from bisect import bisect_left
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().rstrip().split()))
# stack = [-1000000001]

# for a in arr:
#   if stack[-1] < a:
#     stack.append(a)
#   else:
#     stack[bisect_left(stack, a)] = a

# print(len(stack) - 1)

import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().rstrip().split()))
stack = []

for a in arr:
  k = bisect_left(stack, a)
  if len(stack) <= k:
    stack.append(a)
  else:
    stack[k] = a

print(len(stack))