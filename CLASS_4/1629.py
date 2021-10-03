a, b, c = map(int, input().split())

def devide(len):
  if len == 1:
    return a % c
  elif len % 2 == 0:
    left = devide(len // 2)
    return left * left % c
  else:
    left = devide(len // 2)
    return left * left * a % c

print(devide(c))