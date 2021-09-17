'''
Input:
4
1 3 5 7

Output:
3
'''

import sys
import math

# def is_prime_number(x):
#   if x == 1:
#     return False
#   for i in range(2, x):
#     if x % i == 0:
#       return False
#   return True

def is_prime_number(x):
  if x == 1:
    return False
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

count = 0
for number in arr:
  if is_prime_number(number):
    count += 1

print(count)