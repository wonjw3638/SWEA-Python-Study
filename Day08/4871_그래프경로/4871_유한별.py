# 4871_그래프 경로
# 2022-08-18

# 그래프 탐색 dfs
def dfs(now) :
    global visited
    global edges

    visited[now] = 1
    for edge in edges :
        if edge[0] == now and visited[edge[1]] == 0 :
            dfs(edge[1])

T = int(input())

for tc in range(1, T+1) :
    V, E = map(int, input().split())
    edges = []
    for i in range(E) :
        edges.append(list(map(int, input().split())))
    S, G = map(int, input().split())

    visited = [0 for _ in range(V + 1)]
    dfs(S)

    # S로 시작한 완전탐색이 G를 방문했는지 확인
    flag = 1 if visited[G] else 0
    print('#{} {}'.format(tc, flag))