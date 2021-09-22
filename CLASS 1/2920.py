str = list(map(int, input().split()))
if str == sorted(str):
    print('ascending')
elif str == sorted(str, reverse = True):
    print('descending')
else:
    print('mixed')