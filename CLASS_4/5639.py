import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

arr = []
while True:
  try:
    arr.append(int(input().strip()))
  except:
    break

def postorder(arr):
  if len(arr) <= 1:
    return arr
  for i in range(1, len(arr)):
    if arr[i] > arr[0]:
      return postorder(arr[1:i]) + postorder(arr[i:]) + [arr[0]]
  return postorder(arr[1:]) + [arr[0]]

arr = postorder(arr)
for i in arr:
  print(i)