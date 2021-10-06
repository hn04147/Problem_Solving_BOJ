import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
lst = sorted(list(map(int, input().strip().split())))
arr = []

def dfs(idx):
  if len(arr) == m:
    print(*arr)
    return

  for i in range(0, n):
    if len(arr) > 0:
      if lst[i] >= arr[-1]:
        arr.append(lst[i])
        dfs(i)
        arr.pop()
    else:
      arr.append(lst[i])
      dfs(i)
      arr.pop()

dfs(0)