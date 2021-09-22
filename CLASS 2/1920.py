'''
Input:
5
4 1 5 2 3
5
1 3 7 9 5

Output:
1
1
0
0
1
'''

import sys

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

a = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
b = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
for number in numbers:
  if binary_search(arr, number):
    print(1)
  else:
    print(0)