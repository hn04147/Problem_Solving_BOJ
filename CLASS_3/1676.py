n = int(input())
num = 1
for i in range(1, n + 1):
  num *= i

cnt = 0
pos = -1
num = str(num)
while True:
  if num[pos] == '0':
    cnt += 1
    pos -= 1
  else:
    break

print(cnt)