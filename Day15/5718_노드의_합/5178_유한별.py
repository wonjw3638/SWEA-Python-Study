T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nodes = [0 for _ in range(N+1)]
    for _ in range(M):
        node, value = map(int, input().split())
        nodes[node] = value
    for i in range(N-M, 0, -1):
        if i*2 <= N:
            nodes[i] += nodes[i*2]
        if i*2+1 <= N:
            nodes[i] += nodes[i*2+1]
    
    print('#{} {}'.format(tc, nodes[L]))