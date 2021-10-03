import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
zeros = [[0] * (m + 6)]
arr = [] + zeros + zeros + zeros
for _ in range(n):
  arr.append([0, 0, 0] + list(map(int, input().strip().split())) + [0, 0, 0])
arr = arr + zeros + zeros + zeros

shapes = [
        [[0, 1], [0, 2], [0, 3]],
        [[1, 0], [2, 0], [3, 0]],
        [[0, 1], [1, 0], [1, 1]],
        [[1, 0], [2, 0], [2, 1]],
        [[1, 0], [2, 0], [2, -1]],
        [[0, 1], [0, 2], [-1, 2]],
        [[0, 1], [0, 2], [1, 2]],
        [[-1, 0], [-2, 0], [-2, -1]],
        [[-1, 0], [-2, 0], [-2, 1]],
        [[0, -1], [0, -2], [1, -2]],
        [[0, -1], [0, -2], [-1, -2]],
        [[1, 0], [1, 1], [2, 1]],
        [[1, 0], [1, -1], [2, -1]],
        [[0, 1], [-1, 1], [-1, 2]],
        [[0, 1], [1, 1], [1, 2]],
        [[0, 1], [0, 2], [-1, 1]],
        [[0, 1], [0, 2], [1, 1]],
        [[1, 0], [2, 0], [1, 1]],
        [[1, 0], [2, 0], [1, -1]]
        ]

max_value = 0

for i in range(3, n + 3):
  for j in range(3, m + 3):
    for shape in shapes:
      value = arr[i][j]
      for x in shape:
        value += arr[i + x[0]][j + x[1]]
      if value > max_value:
        max_value = value

print(max_value)