visited = []
for _ in range(10):
    a = int(input())
    if a % 42 not in visited:
        visited.append(a%42)
print(len(visited))