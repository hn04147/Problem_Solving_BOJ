import sys

string = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
target_len = len(target)
last_chr = target[-1]
s = []

for i in string:
  s.append(i)
  if i == last_chr:
    if ''.join(s[-target_len:]) == target:
      del s[-target_len:]

s = ''.join(s)

if s:
  print(s)
else:
  print("FRULA")