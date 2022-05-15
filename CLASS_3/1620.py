import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
book_1 = {}
book_2 = {}
for i in range(1, n + 1):
  pk = input().strip()
  book_1[i] = pk
  book_2[pk] = i

for _ in range(m):
  idx = input().strip()
  if idx.isdigit():
    print(book_1[int(idx)])
  else:
    print(book_2[idx])