import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([False for _ in range(n)])

step = 0

while True:
    last = robots.pop()
    robots.appendleft(False)
    belt.appendleft(belt.pop())

    if robots[-1]:
        robots.pop()
        robots.append(False)

    for i in range(n-2, 0, -1):
        if robots[i]:
            if belt[i+1] >= 1 and not robots[i+1]:
                robots[i+1] = True
                robots[i] = False
                belt[i+1] -= 1

    if belt[0] > 0:
        robots.popleft()
        robots.appendleft(True)
        belt[0] -= 1

    step += 1

    zeros = 0
    for i in range(2*n):
        if belt[i] == 0:
            zeros += 1

    if zeros >= k:
        print(step)
        break