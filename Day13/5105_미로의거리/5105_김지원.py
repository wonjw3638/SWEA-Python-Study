# 5105_미로의 거리
# 220826
'''
설계 01:58~02:03
구현 02:04~02:26
'''

import sys
sys.stdin = open('input.txt','rt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# BFS 구현
def bfs(S, G):
    visited = [[0] * (N + 1) for _ in range(N + 1) ]
    queue = [0] * ((N + 1)**2)
    rear = front = -1

    # 시작점 표시
    v = S
    visited[v[0]][v[1]] = 1
    rear += 1
    queue[rear] = v

    # 큐가 비어있으면 멈춤
    while front < rear :
        
        front += 1
        v = queue[front]

        for d in range(4) :
            w = [v[0] + di[d], v[1] + dj[d]]
            # 도착지점에 도착하면 멈춤
            if w == G:
                return visited[v[0]][v[1]] - 1 

            # 인덱스 벗어나는지 확인
            if ((0 <= w[0] < N) and (0 <= w[1] < N)) :
                if map_list[w[0]][w[1]] == '0':
                    # 방문 안한 곳이면 방문, 큐에 push
                    if visited[w[0]][w[1]] == 0:
                        visited[w[0]][w[1]] = visited[v[0]][v[1]] + 1
                        rear += 1
                        queue[rear] = w
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    map_list = list()

    for i in range(N):
        input_list = list(input())
        map_list.append(input_list)
        if '3' in input_list:
            G = [i, input_list.index('3')]
        if '2' in input_list:
            S = [i, input_list.index('2')]

    answer = bfs(S, G)

    print('#{} {}'.format(tc, answer))