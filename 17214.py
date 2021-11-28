# str_ = input()
# opr = ''
# if '+' in str_:
#   opr = '+'
#   arr = str_.split('+')
#   arr[0] = arr[0][:-1]
#   print(f'{int(arr[0]) // 2}xx{opr}{arr[1]}x+W')
# elif '-' in str_:
#   opr = '-'
#   arr = str_.split('-')
#   arr[0] = arr[0][:-1]
#   print(f'{int(arr[0]) // 2}xx{opr}{arr[1]}x+W')
# else:
#   opr = 0
#   arr = str_
#   if 'x' in arr:
#     print(f'{int(arr[:-1]) // 2}xx+W')
#   else:
#     print(f'{arr}x+W')

import collections
eq = input()

def integrate(term):
  t_dic = collections.Counter(term)
  a=term[:len(term)-t_dic["x"]]
  a = int(a) if len(a) != 0 else 1
  
  b = str(a//(t_dic["x"]+1))
  result = b + "x" * (t_dic["x"]+1) if b != "1" else "x" * (t_dic["x"]+1)
  return result

op = ["+","-"]
if eq[0] in op:
  answer = eq[0]
  start = 1
  end = 1
else :
  answer = ""
  start = 0
  end = 0
if eq[start] == "0":
  print("W")
else:
  while end < len(eq):
    if eq[end] not in op:
      end += 1
    else:
      answer += integrate(eq[start:end])
      answer += eq[end]
      start = end + 1
      end += 1
  answer += integrate(eq[start:])+"+W"
  print(answer)