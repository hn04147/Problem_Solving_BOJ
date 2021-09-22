import sys
input = sys.stdin.readline

# def fibonacci(n):
#   global arr
#   if n == 0:
#     return [1, 0]
#   elif n == 1:
#     return [0, 1]
#   else:
#     if arr[n-1] != []:
#       if arr[n-2] != []:
#         arr[n].append(arr[n - 1][0] + arr[n - 2][0])
#         arr[n].append(arr[n - 1][1] + arr[n - 2][1])
#         return [arr[n - 1][0] + arr[n - 2][0], arr[n - 1][1] + arr[n - 2][1]]
#       else:
#         a = fibonacci(n - 2)
#         arr[n].append(arr[n - 1][0] + a[0])
#         arr[n].append(arr[n - 1][1] + a[1])
#         return [arr[n - 1][0] + a[0], arr[n - 1][1] + a[1]]
#     else:
#       if arr[n-2] != []:
#         a = fibonacci(n - 1)
#         arr[n].append(a[0] + arr[n - 2][0])
#         arr[n].append(arr[1] + arr[n - 2][1])
#         return [a[0] + arr[n - 2][0], arr[1] + arr[n - 2][1]]
#       else:
#         a = fibonacci(n - 1)
#         b = fibonacci(n - 2)
#         arr[n].append(a[0] + b[0])
#         arr[n].append(a[1] + b[1])
#         return [a[0] + b[0], a[1] + b[1]]

# n = int(input())
# for _ in range(n):
#   k = int(input())
#   arr = [[] for _ in range(k + 1)]
#   result = fibonacci(k)
#   print(result[0], result[1])

def fibonacci(n):
  zero = [1, 0, 1]
  one = [0, 1, 1]
  length = len(zero)
  if length <= n:
    for i in range(length, n + 1):
      zero.append(zero[i-1] + zero[i-2])
      one.append(one[i-1] + one[i-2])
  print(zero[n], one[n])

n = int(input())
for _ in range(n):
  k = int(input())
  fibonacci(k)