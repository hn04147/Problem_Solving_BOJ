import sys
import heapq
input = sys.stdin.readline

t = int(input().strip())
heap = []
for _ in range(t):
  n = int(input().strip())
  if n == 0:
    try:
      min = heapq.heappop(heap)
      print(min)
    except:
      print(0)
  else:
    heapq.heappush(heap, n)