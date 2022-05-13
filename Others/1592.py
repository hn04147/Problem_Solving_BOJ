n, m, l = map(int,input().split())
people = [0 for _ in range(n)]

cnt = 0
p = 0
while True:
  people[p] += 1
  if people[p] == m:
    print(cnt)
    break
  elif people[p] % 2 != 0:
    p = (p + l) % n
  else:
    p = (p + n - l) % n
  cnt += 1