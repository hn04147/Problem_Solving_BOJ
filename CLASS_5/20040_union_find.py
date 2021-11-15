import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n)]

def find(target):
  if parent[target] == target:
    return target
  else:
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
  a = find(a)
  b = find(b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

ans_exist = False

for i in range(m):
  a, b = map(int, input().rstrip().split())

  a_ = find(a)
  b_ = find(b)

  if a_ == b_:
    print(i + 1)
    ans_exist = True
    break
  else:
    union(a, b)

if not ans_exist:
  print(0)