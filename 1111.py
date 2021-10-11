import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

def get_next():
  if n == 1:
    return "A"
  elif n == 2:
    if arr[0] != arr[1]:
      return "A"
    else:
      return arr[0]
  else:
    try:
      a = (arr[2] - arr[1]) // (arr[1] - arr[0])
      b = arr[1] - arr[0] * a
    except:
      a = 0
      b = arr[1]
    
    for i in range(0, n - 1):
      if arr[i] * a + b != arr[i + 1]:
        return "B"
    
    return int(a * arr[-1] + b)

print(get_next())