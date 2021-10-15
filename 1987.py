import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = [input().rstrip() for _ in range(m)]

visited = []
nums = [[0] * (n) for _ in range(m)]
pprint(nums)