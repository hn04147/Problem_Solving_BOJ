import math
from collections import Counter

n = int(input())
foods = input()

chicken = Counter(foods)['C']
food = n - chicken

print(math.ceil(chicken / (food + 1)))