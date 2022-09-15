# 5105_미로의거리
# 2022-08-25

def bfs():
    global queue
    global q_len

    route = [[0 for _ in range(N)] for _ in range(N)]
    d_i = [0, 0, 1, -1]
    d_j = [1, -1, 0, 0]

    while q_len:
        item = queue.pop(0)
        q_len -= 1
        route[item[0]][item[1]] = item[2]
        # 4방향 탐색
        for k in range(4):
            new_i = item[0] + d_i[k]
            new_j = item[1] + d_j[k]
            # 범위 내의 이동만 확인
            if 0 <= new_i < N and 0 <= new_j < N:
                # 만약 다음 index가 통로 or 도착지이고, 방문한 적 없을 때
                if maze[new_i][new_j] != '1' and route[new_i][new_j] == 0:
                    # 해당 index와 거리를 enqueue
                    queue.append((new_i, new_j, item[2]+1))
                    q_len += 1

    return route[e_i][e_j]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = []
    s_i, s_j = 0, 0
    e_i, e_j = 0, 0
    for i in range(N):
        maze.append(list(input()))
        # 시작 index 찾기
        if '2' in maze[i]:
            s_i = i
            s_j = maze[i].index('2')
        # 도착 index 찾기
        if '3' in maze[i]:
            e_i = i
            e_j = maze[i].index('3')

    queue = [(s_i, s_j, -1)]
    q_len = 1
    
    answer = bfs()
    print('#{} {}'.format(tc, answer))