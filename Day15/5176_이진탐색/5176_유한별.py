def inorder(now):
    global cnt

    if now <= N:
        inorder(now*2)
        visited[now] = cnt
        cnt += 1
        inorder(now*2+1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [0 for _ in range(N+1)]
    cnt = 1
    inorder(1)    
    print('#{} {} {}'.format(tc, visited[1], visited[N//2]))