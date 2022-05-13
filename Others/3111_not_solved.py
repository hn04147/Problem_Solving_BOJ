import sys
input = sys.stdin.readline

# def reverse_string(string): 
#   if len(string) == 0: 
#     return string 
#   else: 
#     return reverse_string(string[1:]) + string[0]

A = input().rstrip()
T = input().rstrip()
# A_reverse = reverse_string(A)
A_reverse = A[::-1]

while True:
  T_length = len(T)
  T = T.replace(A, '', 1)
  if len(T) == T_length:
    break

  T_length = len(T)
#   T = reverse_string(T)
  T = T[::-1]
  T = T.replace(A_reverse, '', 1)
#   T = reverse_string(T)
  T = T[::-1]
  if len(T) == T_length:
    break

print(T)