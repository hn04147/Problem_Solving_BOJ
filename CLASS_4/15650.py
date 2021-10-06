from itertools import combinations

n, m = map(int, input().split())
arr = []

def dfs(cnt):
  if len(arr) == m:
    print(*arr)
    return

  for i in range(cnt, n):
    arr.append(i + 1)
    dfs(i + 1)
    arr.pop()

dfs(0)

# p = combinations(range(1, n + 1), m)
# for i in p:
#   print(*i)