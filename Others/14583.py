import math

h, v = map(float, input().split())

theta = math.atan(v / h)
x = h / (math.cos(theta / 2))
ans1 = x / 2

y1 = h * math.tan(theta / 2)
y2 = v - y1
ans2 = y2 * math.sin((math.pi - theta) / 2)
print(round(ans1, 2), round(ans2, 2))