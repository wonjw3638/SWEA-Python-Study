# 1953_탈주범 검거 문제풀이
# 2022-09-13
from collections import deque

def bfs():
    global visited

    queue = deque()
    # 시작하는 위치의 pipe 정보 queue에 넣어주기
    queue.append((R, C, 1))
    while queue:
        r, c, t = queue.popleft()
        # 방문처리
        if visited[r][c] == 0:
            visited[r][c] = t
        for idx, pipe in enumerate(pipes[table[r][c]]):
            n_r = r + pipe[0]
            n_c = c + pipe[1]
            if 0 <= n_r < N and 0 <= n_c < M:
                # 이미 방문했거나 L개까지 방문했을 때
                if visited[n_r][n_c] or t == L:
                    continue
                # 파이프로 이동했을 때 다음 파이프가 연결 가능한지 확인
                # 각 pipes와 can_connect간 idx 통해 확인
                if table[n_r][n_c] not in can_connect[table[r][c]][idx]:
                    continue
                # 아닐 경우 큐에 append
                else:
                    queue.append((n_r, n_c, t+1))


up = (1, 2, 5, 6)
down = (1, 2, 4, 7)
left = (1, 3, 4, 5)
right = (1, 3, 6, 7)

# 각 파이프에 연결 될 수 있는 파이프
can_connect = [
    [],
    [up, down, left, right,], # 상, 하, 좌, 우 -> 각 연결 가능한 파이프들 목록
    [up, down,], # 상하
    [left, right,], # 좌우
    [up, right], # 상우
    [down, right,], # 하우
    [down, left,], # 하좌
    [up, left,], # 상좌
]    

pipes = [
    [], # 터널 구조물 idx 맞추기
    [(-1, 0), (1, 0), (0, -1), (0, 1)], # 상하좌우
    [(-1, 0), (1, 0)], # 상하
    [(0, -1), (0, 1)], # 좌우
    [(-1, 0), (0, 1)], # 상우
    [(1, 0), (0, 1)], # 하우
    [(1, 0), (0, -1)], # 하좌
    [(-1, 0), (0, -1)], # 상좌
]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    table = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        table.append(list(map(int, input().split())))

    bfs()

    # 갈 수 있는 곳 count 세주기
    answer = 0
    for i in range(N):
        # print(visited[i])
        for j in range(M):
            if visited[i][j]:
                answer += 1

    print('#{} {}'.format(tc, answer))