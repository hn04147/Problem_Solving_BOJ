a = int(input())
for _ in range(a):
    n, str = input().split()
    n = int(n)
    text = ''
    for i in str:
        text += i * n
    print(text)