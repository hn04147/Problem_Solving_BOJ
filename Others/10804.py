list = []
for i in range(1,21):
  list.append(i)
  
for i in range(10):
  a, b = map(int, input().split())
  temp = list[a-1:b]
  temp = reversed(temp)
  list[a-1:b] = temp
  
for i in range(len(list)):
  print(list[i], end = ' ')