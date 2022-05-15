import sys
n, r, c = list(map(int, sys.stdin.readline().split()))
r += 1
c += 1

start, end = 1, (2**n)**2
x_start, x_end = 1, 2**n
y_start, y_end = 1, 2**n

for i in range(n, 0, -1):
  if r <= ((x_start + x_end) // 2) and c <= ((y_start + y_end) // 2):
    end -= 3 * (2**(i-1))**2
    x_end -= 2**(i-1)
    y_end -= 2**(i-1)
  elif r <= ((x_start + x_end) // 2) and c > ((y_start + y_end) // 2):
    start += (2**(i-1))**2
    end -= 2 * (2**(i-1))**2
    x_end -= 2**(i-1)
    y_start += 2**(i-1)
  elif r > ((x_start + x_end) // 2) and c <= ((y_start + y_end) // 2):
    start += 2 * (2**(i-1))**2
    end -= (2**(i-1))**2
    x_start += 2**(i-1)
    y_end -= 2**(i-1)
  else:
    start += 3 * (2**(i-1))**2
    x_start += 2**(i-1)
    y_start += 2**(i-1)
  print(start, end, x_start, x_end, y_start, y_end)

print(start - 1)