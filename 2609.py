'''
Input:
24 18

Output:
6
72
'''

a, b = map(int, input().split())

# for i in range(min(a, b), 0, -1):
#   if a % i == 0 and b % i == 0:
#     print(i)
#     break

# for i in range(max(a, b), (a * b) + 1):
#   if i % a == 0 and i % b == 0:
#     print(i)
#     break

def GCD(x, y):
  while y:
    x, y = y, x % y
  return x

def LCM(x, y):
  result = (x * y) // GCD(x, y)
  return result

print(GCD(a, b))
print(LCM(a, b))