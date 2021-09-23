import sys
input = sys.stdin.readline

def to_ascii(word):
  return ord(word[0]) - 97

# n, m = map(int, input().split())
# group_1, group_2 = [[] for _ in range(26)], [[] for _ in range(26)]
# for _ in range(n):
#   name = input().strip()
#   group_1[to_ascii(name)].append(name)
# for _ in range(m):
#   name = input().strip()
#   group_2[to_ascii(name)].append(name)

# result = []

# for i in range(26):
#   if group_1[i]:
#     for j in range(len(group_1[i])):
#       if group_1[i][j] in group_2[i]:
#         result.append(group_1[i][j])

# print(len(result))
# for i in result:
#   print(i)

n, m = map(int, input().split())
group_1 = [input().strip() for _ in range(n)]
group_2 = [input().strip() for _ in range(m)]

duplicate = list(set(group_1) & set(group_2))
print(len(duplicate))
for i in sorted(duplicate):
  print(i)