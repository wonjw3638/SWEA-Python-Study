def search(y, x, d_y, d_x, n_c):
    n_y = y + d_y
    n_x = x + d_x
    cnt = 0
    flag = False
    while 0 <= n_x < N and 0 <= n_y < N:
        if table[n_y][n_x] != n_c and table[n_y][n_x]:
            cnt += 1
            n_y = n_y + d_y
            n_x = n_x + d_x
        elif table[n_y][n_x] == n_c:
            flag = True
            break
        else:
            cnt = 0
            break
    if flag:
        return cnt
    else:
        return 0


def change_stone(y, x, c):
    global table
    table[y][x] = c
    dir_y = [1, -1, 0, 0, 1, 1, -1, -1]
    dir_x = [0, 0, 1, -1, 1, -1, 1, -1]

    for k in range(8):
        cnt = search(y, x, dir_y[k], dir_x[k], c)
        for change in range(cnt+1):
            table[y+dir_y[k]*change][x+dir_x[k]*change] = c


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    table = [[0 for _ in range(N)] for _ in range(N)]
    table[N//2-1][N//2], table[N//2][N//2-1] = 1, 1
    table[N//2-1][N//2-1], table[N//2][N//2] = 2, 2
    for _ in range(M):
        i, j, color = map(int, input().split())
        change_stone(i-1, j-1, color)

    result = [0, 0]
    for i in range(N):
        for j in range(N):
            if table[i][j]:
                result[table[i][j]-1] += 1
    print('#{}'.format(tc+1), *result)
