import sys
from collections import deque
input = sys.stdin.readline

opers = input().strip()
stack = deque()
answer = ''
prior = {'/': 2, '*': 2, '+': 1, '-': 1, '(': 0}

for s in opers:
  if s.isalpha():
    answer += s
  elif s == '(':
    stack.append(s)
  elif s == ')':
    while True:
      oper = stack.pop()
      if oper == '(':
        break
      answer += oper
  else:
    while stack and prior[stack[-1]] >= prior[s]:
      answer += stack.pop()
    stack.append(s)

while stack: 
  answer += stack.pop()

print(answer)