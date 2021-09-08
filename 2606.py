'''
Input:
7
6
1 2
2 3
1 5
5 2
5 6
4 7

Output: 4
'''

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = []
queue = [1]

while queue:
  num = queue.pop(0)
  if num not in visited:
    visited.append(num)
    for i in graph[num]:
      queue.append(i)

print(len(visited) - 1)
