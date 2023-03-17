import sys
input = sys.stdin.readline

INF = int(1e9)

TC = int(input().rstrip())

for _ in range(TC):
    N, M, W = map(int, input().rstrip().split())
    edges = []
    distance = [INF] * (N+1)

    for _ in range(M):
        S, E, T = map(int, input().rstrip().split())
        edges.append((S-1, E-1, T))
        edges.append((E-1, S-1, T))
    for _ in range(W):
        S, E, T = map(int, input().rstrip().split())
        edges.append((S-1, E-1, -T))
    
    def bellman_ford(start):
        distance[start] = 0
        for i in range(N):
            for edge in edges:
                cur_node = edge[0]
                next_node = edge[1]
                edge_cost = edge[2]
                if distance[next_node] > edge_cost + distance[cur_node]:
                    distance[next_node] = edge_cost + distance[cur_node]
                    if i == N-1:
                        return True
        return False

    negative_cycle = bellman_ford(1)

    print('YES') if negative_cycle else print('NO')
