A, B, C = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(3)]

timeline = [0] * 101
for parking_time in data:
  for i in range(parking_time[0], parking_time[1]):
    timeline[i] += 1

fee = 0
for t in timeline[1:]:
  if t == 1:
    fee += t * A
  elif t == 2:
    fee += t * B
  elif t == 3:
    fee += t * C
print(fee)