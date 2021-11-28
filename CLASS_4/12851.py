from collections import deque

n, m = map(int, input().split())
discovered = [-1 for _ in range(100001)]
paths = [0 for _ in range(100001)]

queue = deque([n])
discovered[n] = 0
paths[n] = 1

while queue:
  loc = queue.popleft()

  for nloc in [loc - 1, loc + 1, 2 * loc]:
    if 0 <= nloc <= 100000:
      if discovered[nloc] == -1:
        discovered[nloc] = discovered[loc] + 1
        paths[nloc] = paths[loc]
        queue.append(nloc)
      else:
        if discovered[nloc] == discovered[loc] + 1:
          paths[nloc] += paths[loc]

print(discovered[m])
print(paths[m])

# n, m = map(int, input().split())
# ans = 0
# cnt = 0
# current_ans = 0
# q = deque([n])
# ans_q = []

# if m <= n:
#   print(n - m)
# else:
#   while True:
#     current_ans += 1

#     for _ in range(len(q)):
#       x = q.popleft()

#       if x - 1 >= 0:
#         if x - 1 == m:
#           ans = current_ans
#           cnt += 1
#         else:
#           q.append(x - 1)
#       if x + 1 <= 100000:
#         if x + 1 == m:
#           ans = current_ans
#           cnt += 1
#         else:  
#           q.append(x + 1)
#       if 2 * x <= 100000:
#         if 2 * x == m:
#           ans = current_ans
#           cnt += 1
#         else:
#           q.append(2 * x)
    
#     if ans != 0:
#       break

#   print(ans)
#   print(cnt)