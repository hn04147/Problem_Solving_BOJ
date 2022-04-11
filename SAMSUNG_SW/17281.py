import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
# 아웃: 0   안타: 1   2루타: 2   3루타: 3   홈런: 4
innings = [list(map(int, input().rstrip().split())) for _ in range(N)]

def cal_score(players):
    score = 0
    player = 0
    for inning in innings:
        out = 0
        first, second, third = 0, 0, 0
        while out < 3:
            if inning[players[player]] == 0:
                out += 1
            elif inning[players[player]] == 1:
                score += third
                third, second, first = second, first, 1
            elif inning[players[player]] == 2:
                score += (third + second)
                third, second, first = first, 1, 0
            elif inning[players[player]] == 3:
                score += (third + second + first)
                third, second, first = 1, 0, 0
            elif inning[players[player]] == 4:
                score += (third + second + first + 1)
                third, second, first = 0, 0, 0
            player = (player + 1) % 9
    return score

ans = 0

for players in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
    players = list(players[:3]) + [0] + list(players[3:])
    ans = max(ans, cal_score(players))

print(ans)