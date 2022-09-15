# 1861_정사각형 방
# 220915

'''
13:20~13:52
'''
import sys
sys.stdin = open('input.txt','rt')
from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def route(i, j):
    global cnt, visit, tmp
    visited[i][j] = visit
    tmp = arr[i][j]
    queue.append([i, j])

    # 1크거나 작으면 이동
    while queue:
        i, j = queue.popleft()
        num = arr[i][j]
        if num < tmp:
            tmp = num
        visited[i][j] = visit
        cnt += 1
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if (0 <= ni < N) and (0 <= nj < N):
                if not visited[ni][nj]:
                    if (arr[ni][nj] == num + 1) or (arr[ni][nj] == num - 1):
                        queue.append([ni, nj])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = room = visit = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            queue = deque()
            visit += 1
            cnt = 0
            route(i, j)
            if answer < cnt:
                answer = cnt
                room = tmp
            if answer == cnt:
                if room > arr[i][j]:
                    room = tmp

    print('#{} {} {}'.format(tc, room, answer))