'''
Input:
121
1231
12421
0

Output:
yes
no
yes
'''
while True:
  a = int(input())
  if a == 0:
    break
  else:
    a = str(a)

  idx = 0
  length = len(a)
  result = 'yes'
  while idx < (len(a) // 2):
    if a[idx] != a[length - idx - 1]:
      result = 'no'
      break
    idx += 1
  print(result)