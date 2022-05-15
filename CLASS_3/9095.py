#dp(num) = dp(num-1) + dp(num-2) + dp(num-3)

list_ = [0] * 12

def solution(num):
    global list_
    if num==1: return 1
    if num==2: return 2
    if num==3: return 4
    if list_[num]!=0: return list_[num]
    list_[num] = solution(num-1) + solution(num-2) + solution(num-3)
    return list_[num]

num = int(input())
for i in range (0, num):
    index = int(input())
    print(solution(index))

