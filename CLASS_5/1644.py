n = int(input())

def prime_list(n):
  sieve = [True] * n
  
  m = int(n ** 0.5)
  for i in range(2, m + 1):
    if sieve[i] == True:
      for j in range(i + i, n, i):
        sieve[j] = False
  
  return [i for i in range(2, n) if sieve[i] == True]

arr = prime_list(n + 1)
cnt = 0

for i in range(0, len(arr)):
  sum_ = 0
  idx = i
  while sum_ <= n and idx < len(arr):
    sum_ += arr[idx]
    if sum_ == n:
      cnt += 1
      break
    idx += 1

print(cnt)