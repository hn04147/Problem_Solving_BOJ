import sys
input = sys.stdin.readline

gears = [[int(i) for i in input().rstrip()] for _ in range(4)]
status = [[0, 2, 6] for _ in range(4)]

def rotate(num, dir):
  if dir == 1:
    idx = []
    idx.append(gears[num][7])
    for i in gears[num][:7]:
      idx.append(i)
    gears[num] = idx
  else:
    idx = []
    for i in gears[num][1:]:
      idx.append(i)
    idx.append(gears[num][0])
    gears[num] = idx

def step(gear_num, dir, lrb):
  if lrb == 'both' or lrb == 'left':
    if gear_num > 0:
      if gears[gear_num-1][2] != gears[gear_num][6]:
        step(gear_num-1, dir*-1, 'left')
  if lrb == 'both' or lrb == 'right':
    if gear_num < 3:
      if gears[gear_num+1][6] != gears[gear_num][2]:
        step(gear_num+1, dir*-1, 'right')
  rotate(gear_num, dir)

n = int(input())
for _ in range(n):
  k, dir = map(int, input().rstrip().split())
  step(k-1, dir, 'both')

print(gears[0][0] + gears[1][0]*2 + gears[2][0]*4 + gears[3][0]*8)