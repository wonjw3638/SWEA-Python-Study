# 5251 최소 이동 거리
# 220929

'''
설계시간 09:41~09:45
구현시간 09:46~10:03
'''

import sys
sys.stdin = open('input.txt', 'r')

# 목표지점, 출발지점, edge정보, node까지 가는 최소값
def dijkstra(N, X, adj, d):
		# 출발점 ~ i까지 최소값
    for i in range(N+1):
        d[i] = adj[X][i]
    
    U = [X]
    # 노드 개수 만큼 탐색
    for _ in range(N+1):
        # 가중치 최소값 찾기
        tmp = 100
        for i in range(1, N+1):
            if (i not in U) and d[i] < tmp:
                tmp = d[i]
                w = i
        # 방문표시
        U.append(w)
        # 인접한 노드가 있을 때, 인접한 노드를 통해 가는게 빠른지, 바로 가는게 빠른지 탐색
        for v in range(1, N+1):
            if 0 < adj[w][v] < 100:
                d[v] = min(d[v], d[w] + adj[w][v])
        
    # 도착지점까지 가는 최소값
    return d[N]


T = int(input())

for tc in range(1, T + 1):
    N, E = list(map(int, input().split()))
    edge = [[100]*(N+1) for _ in range(N+1)]

    for i in range(N+1):
        edge[i][i] = 0

    for _ in range(E):
        n1, n2, w = list(map(int, input().split()))
        edge[n1][n2] = w

    dout = [0] * (N+1)
    answer = dijkstra(N, 0, edge, dout)

    print('#{} {}'.format(tc, answer))