import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
arr_ = sorted(set(arr))
dic = {}
for i in range(len(arr_)):
  dic[arr_[i]] = i
for i in arr:
  print('{} '.format(dic[i]), end = '')