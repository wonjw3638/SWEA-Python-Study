T = int(input())
INF = float('INF')

def dfs(now, depth):
    global answer
    global tmp

    if depth == N-1:
        tmp += graph[now][0]
        answer = min(answer, tmp)
        tmp -= graph[now][0]
        return
    
    for i in range(N):
        if visited[i]:
            continue
        tmp += graph[now][i]
        visited[i] = True
        dfs(i, depth+1)
        tmp -= graph[now][i]
        visited[i] = False


for tc in range(1, T+1):
    N = int(input())
    graph = []
    visited = [False for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    tmp = 0
    answer = INF
    visited[0] = True
    dfs(0, 0)

    print('#{} {}'.format(tc, answer))