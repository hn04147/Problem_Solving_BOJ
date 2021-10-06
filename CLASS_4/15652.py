n, m = map(int, input().split())
arr = []

def dfs(cnt):
  if len(arr) == m:
    print(*arr)
    return

  for i in range(cnt, n + 1):
    arr.append(i)
    dfs(i)
    arr.pop()

dfs(1)