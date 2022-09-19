def dfs(now):
    global cnt
    
    for edge in edges[now]:
        if visited[edge]:
            continue
        dfs(edge)
    cnt += 1

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    input_arr = list(map(int, input().split()))
    edges = [[] for _ in range(E+2)]
    visited = [False for _ in range(E+2)]
    for i in range(E):
        edges[input_arr[i*2]].append(input_arr[i*2+1])
    cnt = 0
    dfs(N)
    print('#{} {}'.format(tc, cnt))