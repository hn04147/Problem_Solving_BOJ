n = int(input())
arr = [0 for _ in range((n + 1) if n >= 3 else 4)]
nums = [0 for _ in range((n + 1) if n >= 3 else 4)]
arr[1], arr[2], arr[3] = 0, 1, 1
nums[1], nums[2], nums[3] = 0, 1, 1

if n == 1:
  print(1)
  print(1)
elif 1 < n <= 3:
  print(arr[n])
  print(n, 1)
else:
  for i in range(4, n + 1):
    arr[i] = arr[i - 1] + 1
    nums[i] = i - 1
    if i % 3 == 0:
      nums[i] = i // 3 if (arr[i // 3] + 1) < arr[i] else nums[i]
      arr[i] = min((arr[i // 3] + 1), arr[i])
    if i % 2 == 0:
      nums[i] = i // 2 if (arr[i // 2] + 1) < arr[i] else nums[i]
      arr[i] = min((arr[i // 2] + 1), arr[i])
  print(arr[-1])

  result = [n]
  pos = n
  while True:
    pos = nums[pos]
    result.append(pos)
    if pos == 1:
      break
  
  print(*result)