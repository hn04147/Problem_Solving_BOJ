import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())

l_hq, r_hq = [], []

for step in range(n):
    if (step + 1) % 2 == 1:
        heapq.heappush(l_hq, -int(input().rstrip()))
    else:
        heapq.heappush(r_hq, int(input().rstrip()))
    
    if step == 0:
        print(-l_hq[0])
    else:
        if -l_hq[0] > r_hq[0]:
            temp = -heapq.heappop(l_hq)
            heapq.heappush(l_hq, -heapq.heappop(r_hq))
            heapq.heappush(r_hq, temp)

        if (step + 1) % 2 == 1:
            print(-l_hq[0])
        else:
            print(min(-l_hq[0], r_hq[0]))

# heapq 하나로 관리하면 시간초과
# left heapq, right heapq 두 가지로 관리
# left heapq는 최대힙, right heapq는 최소힙으로 나누어 관리

# hq = []

# for step in range(n):
#     k = int(input().rstrip())
#     heapq.heappush(hq, k)
#     temp_hq = []

#     if (step+1) % 2 == 1:
#         for _ in range(step//2):
#             heapq.heappush(temp_hq, heapq.heappop(hq))
#         ans = heapq.heappop(hq)
#         print(ans)
#         heapq.heappush(hq, ans)
#         while temp_hq:
#             heapq.heappush(hq, heapq.heappop(temp_hq))

#     else:
#         for _ in range((step-1)//2):
#             heapq.heappush(temp_hq, heapq.heappop(hq))
#         ans_1 = heapq.heappop(hq)
#         ans_2 = heapq.heappop(hq)
#         print(min(ans_1, ans_2))
#         heapq.heappush(hq, ans_1)
#         heapq.heappush(hq, ans_2)
#         while temp_hq:
#             heapq.heappush(hq, heapq.heappop(temp_hq))
