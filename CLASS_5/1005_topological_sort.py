import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
INF = sys.maxsize

def topological_sort(graph, degree):
  s = deque()
  length = len(degree) - 1
  ans = []

  for i in range(1, length + 1):
    if degree[i] == 0:
      s.append(i)
      degree[i] = -1
  
  for i in range(length):
    element = s.pop()
    ans.append(element)
    for j in range(len(graph[element])):
      degree[graph[element][j]] -= 1
    for j in range(1, length + 1):
      if degree[j] == 0:
        s.append(j)
        degree[j] = -1

  return ans

for _ in range(T):
  n, k = map(int, input().rstrip().split())
  arr = [0] + list(map(int, input().rstrip().split()))
  graph = [[] for _ in range(n + 1)]
  graph_reverse = [[] for _ in range(n + 1)]
  degree = [0 for _ in range(n + 1)]
  for _ in range(k):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph_reverse[y].append(x)
    degree[y] += 1
  w = int(input())

  tp = topological_sort(graph, degree)
  dp = [0 for _ in range(n + 1)]

  for i in range(0, n):
    max_ = 0
    this = tp[i]

    if len(graph_reverse[this]) == 0:
      dp[this] = arr[this]
    else:
      for j in range(len(graph_reverse[this])):
        max_ = max(max_, dp[graph_reverse[this][j]])
      dp[this] = max_ + arr[this]

  print(dp[w])