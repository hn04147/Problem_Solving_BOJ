import sys
from collections import Counter
input = sys.stdin.readline

arr = []
sum = 0
n = int(input())
for _ in range(n):
  idx = int(input())
  arr.append(idx)
  sum += idx
arr.sort()

def modefinder(num):
  c = Counter(num)
  order = c.most_common()
  maximum = order[0][1]

  modes = []
  for num in order:
    if num[1] == maximum:
      modes.append(num[0])

  return modes

mode_arr = sorted(modefinder(arr))

print(round(sum / n))
print(arr[n // 2])
print(mode_arr[1] if len(mode_arr) > 1 else mode_arr[0])
print(max(arr) - min(arr))