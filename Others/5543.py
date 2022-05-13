burger = []
drink = []
for i in range(3):
  temp = int(input())
  burger.append(temp)
for i in range(2):
  temp = int(input())
  drink.append(temp)

cheap = 10000
for i in range(3):
  for j in range(2):
    if burger[i] + drink[j] - 50 < cheap:
      cheap = burger[i] + drink[j] - 50

print(cheap)