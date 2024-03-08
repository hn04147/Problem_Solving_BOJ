# [1 1]^n = [F(n+1)  Fn]
# [1 0]     [Fn  F(n-1)]

# [F(n+1)] = [1 1]^n[1]
# [ F(n) ]   [1 0]  [0]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

def matrix_mul(a, b):
    e00 = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000007
    e01 = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000007
    e10 = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000007
    e11 = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000007

    return [
        [e00, e01],
        [e10, e11]
    ]

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        F = power([[1, 1], [1, 0]], n-1)
        return F[0][0]

def power(m, n):
    if n == 1:
        return m
    elif n == 2:
        return matrix_mul(m, m)
    else:
        tmp = power(m, n//2)
        if n % 2 == 0:
            return matrix_mul(tmp, tmp)
        else:
            return matrix_mul(matrix_mul(tmp, tmp), m)

ans = fibonacci(n)
print(ans)