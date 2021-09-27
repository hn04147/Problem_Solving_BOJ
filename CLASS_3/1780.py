'''
Input:
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1

Output:
10
12
11
'''

import sys
input = sys.stdin.readline

t = int(input().strip())
paper = [list(map(int, input().strip().split())) for _ in range(t)]
type = [0, 0, 0]

def check_paper(x, y, width):
  color = paper[x][y]
  for i in range(x, x + width):
    for j in range(y, y + width):
      if paper[i][j] != color:
        return [False, 2]
  return [True, color]

def check(x, y, width):
  result, color = check_paper(x, y, width)
  if result:
    type[color] += 1
  else:
    x = x + 1
    y = y + 1
    new_width = width // 3
    for i in range(x, x + width, new_width):
      for j in range(y, y + width, new_width):
        check(i - 1, j - 1, new_width)
  
check(0, 0, t)

print('{}\n{}\n{}'.format(type[-1], type[0], type[1]))