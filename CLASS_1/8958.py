n = int(input())
for _ in range(n):
    str = input()
    result = 0
    count = 0
    for i in str:
        if i == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)