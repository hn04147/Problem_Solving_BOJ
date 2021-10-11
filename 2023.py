import math

n = int(input())
one_digit_prime_number = ['2', '3', '5', '7']

def is_prime_number(x):
  if x == 1:
    return False
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

# if n == 1:
#   print(*one_digit_prime_number, sep = '\n')
# else:
#   for i in range(int('2' + '0' * (n - 1)), int('8' + '0' * (n - 1))):
#     if str(i)[:1] in one_digit_prime_number:
#       is_prime = True
#       for j in range(2, n):
#         if not is_prime_number(int(str(i)[:j])):
#           is_prime = False
#           break
#       if is_prime and is_prime_number(i):
#         print(i)


def find_prime(num):
  if len(num) == 0:
    for i in range(2, 8):
      idx = num + str(i)
      if is_prime_number(int(idx)):
        if len(idx) == n:
          print(idx)
        else:
          num += str(i)
          find_prime(num)
          num = num[:-1]
  else:
    for i in range(0, 10):
      idx = num + str(i)
      if is_prime_number(int(idx)):
        if len(idx) == n:
          print(idx)
        else:
          num += str(i)
          find_prime(num)
          num = num[:-1]
  

find_prime('')