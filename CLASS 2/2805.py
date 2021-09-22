import sys
input = sys.stdin.readline

n, l = map(int, input().split())
trees = list(map(int, input().split()))

def usable_tree_length(trees, length):
  result = 0
  for tree in trees:
    if tree > length:
      result += (tree - length)
  return result

start = 0
end = max(trees)
while start <= end:
  mid = (start + end) // 2
  if usable_tree_length(trees, mid) >= l:
    start = mid + 1
  else:
    end = mid - 1
  
print(end)