def prime_list(n):
  sieve = [True] * n
  m = int(n ** 0.5)

  for i in range(2, m + 1):
    if sieve[i] == True:
      for j in range(i + i, n, i):
        sieve[j] = False

  return [i for i in range(2, n) if sieve[i] == True]

a, b = map(int, input().split())

list = prime_list(b + 1)
for num in list:
  if num >= a and num != 1:
    print(num)