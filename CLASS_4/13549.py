from collections import deque

n, k = map(int, input().split())
visited = [0] * (100001)

q = deque()
q.append([n, 0])
visited[n] = 1

while q:
  pos, cnt = q.popleft()
  if pos == k:
    break
  if (2 * pos) <= 100000:
    if visited[2 * pos] == 0:
      visited[2 * pos] = 1
      q.append([2 * pos, cnt])
  if (pos - 1) >= 0:
    if visited[pos - 1] == 0:
      visited[pos - 1] = 1
      q.append([pos - 1, cnt + 1])
  if (pos + 1) <= 100000:
    if visited[pos + 1] == 0:
      visited[pos + 1] = 1
      q.append([pos + 1, cnt + 1])

print(cnt)