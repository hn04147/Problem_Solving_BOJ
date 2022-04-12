import sys
from itertools import permutations
from pprint import pprint
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
rcs = [list(map(int, input().rstrip().split())) for _ in range(K)]
graph_copy = [[0 for _ in range(M)] for _ in range(N)]


def get_value(arr):
    return min([sum(i) for i in arr])

def rotate(r, c, s):
    for i in range(s, 0, -1):
        x, y, h = r-i, c-i, i*2+1
        # print(f'({x}, {y}, {h})')
        first = graph_copy[x][y]
        for j in range(h-1):
            graph_copy[x+j][y] = graph_copy[x+j+1][y]
        for j in range(h-1):
            graph_copy[x+h-1][y+j] = graph_copy[x+h-1][y+j+1]
        for j in range(h-1, 0, -1):
            graph_copy[x+j][y+h-1] = graph_copy[x+j-1][y+h-1]
        for j in range(h-1, 0, -1):
            graph_copy[x][y+j] = graph_copy[x][y+j-1]
        graph_copy[x][y+1] = first

ans = 10000000

for p in list(permutations(range(K))):
    # print('permutation: ', p)
    for i in range(N):
        for j in range(M):
            graph_copy[i][j] = graph[i][j]
    for idx in p:
        r, c, s = rcs[idx]
        rotate(r-1, c-1, s)
        # pprint(graph)
    ans = min(ans, get_value(graph_copy))

print(ans)