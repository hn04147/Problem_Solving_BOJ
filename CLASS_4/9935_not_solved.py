import sys

string = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
target_len = len(target)
s = ""

for i in string:
  s += i
  if len(s) >= target_len:
    if s[-target_len:] == target:
      s = s[:(len(s) - target_len)]

if s:
  print(s)
else:
  print("FRULA")