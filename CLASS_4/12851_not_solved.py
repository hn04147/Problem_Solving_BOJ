from collections import deque

n, k = map(int, input().split())
visited = [0] * (100001)

q = deque()
q.append([n, 0])
visited[n] = 1
found_ans = False
answer = 0
cnt = 0
count = 0

while q:
  pos, cnt = q.popleft()
  if not found_ans:
    if pos == k:
      answer = cnt
      count += 1
      found_ans = True
  else:
    if cnt > answer:
      break
    elif cnt == answer:
      count += 1

  if (2 * pos) <= 100000:
    if visited[2 * pos] == 0:
      if not found_ans:
        visited[2 * pos] = 1
        q.append([2 * pos, cnt + 1])
      else:
        if (cnt + 1) < answer:
          q.append([2 * pos, cnt + 1])
  if (pos - 1) >= 0:
    if visited[pos - 1] == 0:
      if not found_ans:
        visited[pos - 1] = 1
        q.append([pos - 1, cnt + 1])
      else:
        if (cnt + 1) < answer:
          q.append([pos - 1, cnt + 1])
  if (pos + 1) <= 100000:
    if visited[pos + 1] == 0:
      if not found_ans:
        visited[pos + 1] = 1
        q.append([pos + 1, cnt + 1])
      else:
        if (cnt + 1) < answer:
          q.append([pos + 1, cnt + 1])

print(answer)
print(count)