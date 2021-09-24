import sys

A, B, V = map(int,sys.stdin.readline().split())

if (V-A)%(A-B) == 0:
    print(int((V-A)/(A-B))+1)
else:
    print(int((V-A)/(A-B))+2)