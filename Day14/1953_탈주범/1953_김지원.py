# 1953_탈주범
# 220915
from collections import deque
import sys
sys.stdin = open('input.txt','rt')

T = int(input())

# 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 델타 인덱스
pipeline = {
    1 : [0, 1, 2, 3],
    2 : [0, 2],
    3 : [1, 3],
    4 : [0, 1],
    5 : [1, 2],
    6 : [2, 3],
    7 : [0, 3],
}

# 델타 인덱스 진행 후에 올수 없는 파이프 유형
cantgo = {
    0 : [3, 4, 7],
    1 : [2, 4, 5],
    2 : [3, 5, 6],
    3 : [2, 6, 7],
}

def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    cnt = 0

    while queue:
        i, j = queue.popleft()
        D = pipeline.get(arr[i][j])
        # 파이프가 존재 하는 곳
        if D:
            cnt += 1
            if visited[i][j] < L:
                for d in D:
                    ni = i + di[d]
                    nj = j + dj[d]
                    # 인덱스 범위 체크
                    if (0 <= ni < N) and (0 <= nj < M):
                        # 방문하지 않는 점
                        if not visited[ni][nj]:
                            # 다음에 올 수 없는 파이프가 아닌 경우에
                            if not (arr[ni][nj] in cantgo.get(d)):
                                visited[ni][nj] = visited[i][j] + 1
                                queue.append([ni, nj])
    
    return cnt


for tc in range(1, T+1):
    N, M, R, C, L = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = bfs(R, C)

    print('#{} {}'.format(tc, answer))