import sys
import heapq
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  n = int(input().strip())
  max_heap = []
  min_heap = []
  for _ in range(n):
    O, num = input().strip().split()
    num = int(num)

    if O == 'I':
      heapq.heappush(min_heap, num)
      heapq.heappush(max_heap, [-num, num])
    else:
      if num == -1:
        try:
          a = heapq.heappop(min_heap)
          idx = max_heap.index([-a, a])
          del max_heap[idx]
        except:
          continue
      else:
        try:
          a = heapq.heappop(max_heap)
          idx = min_heap.index(a[1])
          del min_heap[idx]
        except:
          continue
  
  if min_heap:
    print(heapq.heappop(max_heap)[1], heapq.heappop(min_heap))
  else:
    print('EMPTY')