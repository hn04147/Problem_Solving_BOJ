import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
input = lambda : sys.stdin.readline().rstrip()

N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

l_arr, r_arr = arr[:N//2], arr[N//2:]
l_sum, r_sum = [], []
ans = 0

for i in range(1, len(l_arr)+1):
    for c in list(combinations(l_arr, i)):
        l_sum.append(sum(c))
for i in range(1, len(r_arr)+1):
    for c in list(combinations(r_arr, i)):
        r_sum.append(sum(c))

l_sum.sort()
r_sum.sort()

def count_num(nums, find_value):
    return bisect_right(nums, find_value) - bisect_left(nums, find_value)

for l in l_sum:
    ans += count_num(r_sum, S - l)

ans += count_num(l_sum, S)
ans += count_num(r_sum, S)

print(ans)