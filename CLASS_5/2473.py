import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().rstrip().split())))

ans = []
min_value = sys.maxsize

for i in range(0, n - 2):
  l = i + 1
  r = n - 1
  while l != r:
    if abs(arr[i] + arr[l] + arr[r]) < min_value:
      min_value = abs(arr[i] + arr[l] + arr[r])
      ans = [i, l, r]
    if arr[i] + arr[l] + arr[r] < 0:
      l += 1
    elif arr[i] + arr[l] + arr[r] > 0:
      r -= 1
    else:
      print(arr[ans[0]], arr[ans[1]], arr[ans[2]])
      sys.exit()

print(arr[ans[0]], arr[ans[1]], arr[ans[2]])