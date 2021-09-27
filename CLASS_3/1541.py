'''
Input:
55-50+40

Output:
-35
'''

import sys
input = sys.stdin.readline

a = input().strip()
nums = list(a.split('-'))

def get_sum(str_):
  if '+' in str_:
    arr = list(map(int, str_.split('+')))
    sum_ = 0
    for i in arr:
      sum_ += i
    return sum_
  else:
    return int(str_)

answer = 0

for i in range(len(nums)):
  if i == 0:
    answer = get_sum(nums[i])
  else:
    answer -= get_sum(nums[i])

print(answer)