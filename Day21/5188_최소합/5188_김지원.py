# 5188 최소합
# 220921

'''
시작시각 18:27
종료시각 
'''
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

di = [1, 0]
dj = [0, 1]

def bfs(i, j):
    queue = deque()
    visited[i][j] = arr[i][j]
    queue.append([i, j])

    while queue:
        i , j = queue.popleft()

        for d in range(2):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    queue.append([ni,nj])
                else:
                    visited[ni][nj] = min(visited[i][j] + arr[ni][nj], visited[ni][nj])
    
    return visited[N-1][N-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    answer = bfs(0, 0)

    print('#{} {}'.format(tc, answer))