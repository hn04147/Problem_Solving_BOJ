import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
jewels = []
for _ in range(n):
    heapq.heappush(jewels, list(map(int, input().rstrip().split()))) 
bags = [int(input().rstrip()) for _ in range(k)]
bags.sort()

ans = 0
hq = []

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        m, v = heapq.heappop(jewels)
        heapq.heappush(hq, -v)

    if hq:
        v = -heapq.heappop(hq)
        ans += v
    elif not jewels:
        break

print(ans)