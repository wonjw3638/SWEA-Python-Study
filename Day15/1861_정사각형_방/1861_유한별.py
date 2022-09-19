from collections import deque

# bfs 구현
def bfs(i, j):
    global dp

    queue = deque()
    # 시작 방 count = 1
    queue.append((i, j, 1))
    max_move = 1
    # queue를 활용해 갈 수 있는 곳 전체 탐색
    while queue:
        q_i, q_j, q_cnt = queue.popleft()
        # 현 위치에서 4방향 탐색
        for k in range(4):
            n_i = q_i + d_i[k]
            n_j = q_j + d_j[k]
            # 다음 스텝이 범위 내에 존재하는지 확인
            if 0 <= n_i < N and 0 <= n_j < N:
                # 만약 건너갈 수 있는 조건을 만족한다면
                if rooms[n_i][n_j] == rooms[q_i][q_j] + 1:
                    # 건너가는 방이 이미 최적해를 가지고 있다면 해당 최적해 + 그 방까지의 거리 저장
                    if dp[n_i][n_j]:
                        max_move = max(max_move, q_cnt+dp[n_i][n_j])
                    # 그게 아닐 경우 그 방까지의 거리 저장
                    else:
                        queue.append((n_i, n_j, q_cnt+1))
                        max_move = max(max_move, q_cnt+1)
    # 저장된 거리 중 가장 먼 곳(최적해)을 dp 테이블에 반영
    dp[i][j] = max_move

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = []
    dp = [[0 for _ in range(N)] for _ in range(N)]

    d_i = [0, 0, 1, -1]
    d_j = [1, -1, 0, 0]

    for _ in range(N):
        rooms.append(list(map(int, input().split())))

    # N*N 전체 탐색(by bfs)
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    # dp 중 max값을 찾고, 해당 값이 max 일 경우 가장 작은 값을 가진 방을 찾음
    max_i, max_j, max_v = 0, 0, 0
    for i in range(N):
        for j in range(N):
            if max_v <= dp[i][j]:
                max_v = dp[i][j]
                if dp[max_i][max_j] != dp[i][j]:
                    max_i = i
                    max_j = j
                if rooms[max_i][max_j] > rooms[i][j]:
                    max_i = i
                    max_j = j 
    # 생각해보니 map과 max를 활용해 dp table의 최댓값을 구하고, N*N 탐색을 통해 room의 값만 비교해줘서 저장했어도 됐을 듯

    # 출력부
    print('#{} {} {}'.format(tc, rooms[max_i][max_j], max_v))