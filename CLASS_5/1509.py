import sys
input = sys.stdin.readline

string = input().rstrip()
palindrome = [[0 for _ in range(len(string))] for _ in range(len(string))]
length = len(string)

# To fill the dp array which means 
#   the string from palindrome[i] to palindrome[j] is palindrome
for i in range(length):
    palindrome[i][i] = 1
for i in range(length-1):
    if string[i] == string[i+1]:
        palindrome[i][i+1] = 1
for j in range(2, length):
    for i in range(length-j):
        if string[i] == string[i+j] and palindrome[i+1][i+j-1]:
            palindrome[i][i+j] = 1

p = [2500 for _ in range(length)]
p[0] = 1
p[1] = 1 if palindrome[0][1] else 2

for end in range(2, length):
    if palindrome[0][end]:
        p[end] = 1
        continue
    for start in range(1, end+1):
        if palindrome[start][end]:
            p[end] = min(p[end], p[start-1] + 1)
        else:
            p[end] = min(p[end], p[start-1] + end + start - 1)

print(p[-1])