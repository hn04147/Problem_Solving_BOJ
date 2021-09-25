import sys
import heapq
input = sys.stdin.readline

t = int(input().strip())
heap = []
for _ in range(t):
  n = int(input().strip())
  if n == 0:
    try:
      value = heapq.heappop(heap)
      print(value[1])
    except:
      print(0)
  else:
    heapq.heappush(heap, [-n, n])