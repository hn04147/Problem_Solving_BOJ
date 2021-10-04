a, b, c = map(int, input().split())

def devide(len):
  if len == 1:
    return a % c
  else:
    left = devide(len // 2)
    if len % 2 == 0:
      return left * left % c
    else:
      return left * left * a % c

print(devide(b))