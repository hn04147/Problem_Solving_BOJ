'''
Input:
5 17

Output:
4
'''

from collections import deque

n, k = map(int, input().split())
queue = deque()
queue.append(n)
count = 0
is_continue = True

def three_positions(n):
  return [2*n, n+1, n-1]

while is_continue:
  count += 1
  for _ in range(len(queue)):
    current_pos = queue.popleft()
    new_pos = three_positions(current_pos)
    if k in new_pos:
      is_continue = False
    for pos in new_pos:
      if 0 <= pos <= 100000:
        queue.append(pos)

print(count)