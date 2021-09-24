def return_producer(num):
  num_ = str(num)
  for i in num_:
    num += int(i)
  return num

a = int(input())
result = 1

while True:
  if a < result:
    result = 0
    break
  if return_producer(result) == a:
    break
  else:
    result += 1

print(result)