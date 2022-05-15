import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
dict = {}
for _ in range(n):
  a, b = input().strip().split()
  dict[a] = b

for _ in range(m):
  a = input().strip()
  print(dict[a])