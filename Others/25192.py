import sys
input = sys.stdin.readline

n = int(input().rstrip())
names = set()
result = 0

for _ in range(n):
    name = input().rstrip()
    if name == 'ENTER':
        names.clear()
    else:
        if name not in names:
            names.add(name)
            result += 1
print(result)