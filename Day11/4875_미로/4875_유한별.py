# 4875_미로
# 2022-08-23

def dfs(y, x):
    global flag
    global maze

    # 도착했을 때 처리
    if maze[y][x] == '3':
        flag = 1
        return

    # 4방향 델타검색
    maze[y][x] = '1'
    for d in range(4):
        new_x = x + d_x[d]
        new_y = y + d_y[d]
        # 들어갈 수 있는 길이면 (0 이나 3)
        if 0 <= new_x < N and 0 <= new_y < N:
            if maze[new_y][new_x] != '1':
                dfs(new_y, new_x)
                # 만약 이미 3에 도달했었으면 더 이상 탐색 X
                if flag: return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = []
    flag = 0
    start_idx = -1
    d_x = [0, 0, 1, -1]
    d_y = [1, -1, 0, 0]

    for i in range(N):
        maze.append(list(input()))
        # 시작 index 찾기
        for j in range(N):
            if maze[i][j] == '2':
                start_idx = (i, j)

    # dfs 시작
    dfs(start_idx[0], start_idx[1])

    print('#{} {}'.format(tc, flag))