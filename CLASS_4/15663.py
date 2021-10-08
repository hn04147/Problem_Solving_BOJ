import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
lst = sorted(list(map(int, input().strip().split())))
arr = []
visited = [False] * n
answer = []

def dfs(idx):
  if len(arr) == m:
    answer_ = []
    for i in arr:
      answer_.append(i)
    answer.append(answer_)
    return

  for i in range(0, n):
    if len(arr) > 0:
      if not visited[i]:
        arr.append(lst[i])
        visited[i] = True
        dfs(i)
        arr.pop()
        visited[i] = False
    else:
      arr.append(lst[i])
      visited[i] = True
      dfs(i)
      arr.pop()
      visited[i] = False

dfs(0)

for i in range(len(answer)):
  if answer[i] not in answer[:i]:
    print(*answer[i])