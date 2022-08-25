# 1226_미로1
# 2022-08-25

def dfs(i, j):
    global result
    global visited

    visited[i][j] = 1
    # 목표에 도착했을시
    if maze[i][j] == '3':
        result = 1
        return
    
    # 4방향 델타탐색
    for k in range(4):
        new_i = i + d_i[k]
        new_j = j + d_j[k]
        # 범위 내의 index이고 해당 위치가 벽이 아닐 때
        if 0 <= new_i < 16 and 0 <= new_j < 16:
            if visited[new_i][new_j] == 0 and maze[new_i][new_j] != '1':
                # 재귀함수 호출
                dfs(new_i, new_j)
                if result:
                    return

while True:
    T = int(input())
    maze = list()
    for i in range(16):
        maze.append(list(input()))
        if '2' in maze[i]:
            idx = (i, maze[i].index('2'))
    visited = [[0 for _ in range(16)] for _ in range(16)]
    d_i = [0, 0, 1, -1]
    d_j = [1, -1, 0, 0]
    result = 0

    dfs(idx[0], idx[1])
    print('#{} {}'.format(T, result))
    if T == 10:
        break