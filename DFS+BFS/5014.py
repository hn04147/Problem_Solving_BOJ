from collections import deque

f, s, g, u, d = map(int, input().split())
q = deque([s])
visited = [False for _ in range(f + 1)]
visited[s] = True
cnt = 0

def bfs():
  global cnt

  if s == g:
    print(0)
    return

  while q:
    cnt += 1
    for _ in range(len(q)):
      x = q.popleft()
      for i in [x + u, x - d]:
        if 1 <= i <=f:
          if visited[i] == False:
            if i == g:
              print(cnt)
              return
            else:
              visited[i] = True
              q.append(i)

  print('use the stairs')
  return

bfs()