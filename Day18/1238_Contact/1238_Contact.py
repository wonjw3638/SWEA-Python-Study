import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
T = 10
for tc in range(1, T+1):
    # 방문 처리와 연락 거리 저장
    visited = [-1 for _ in range(101)]
    # bfs를 구현하기 위한 queue
    queue = deque()
    # 간선 정보 저장할 2차원 list
    edges = [[] for _ in range(101)]

    N, S = map(int, input().split())
    input_data = list(map(int, input().split()))
    idx = 0
    while idx < N:
        edges[input_data[idx]].append(input_data[idx+1])
        idx += 2
    visited[S] = 0

    # S에서 나가는 첫 연락을 queue에 append
    for edge in edges[S]:
        queue.append((S, edge))
    # bfs
    while queue:
        f, t = queue.popleft()
        if visited[t] == -1:
            visited[t] = visited[f] + 1
            for edge in edges[t]:
                queue.append((t, edge))
    
    # max값을 찾아 인덱스 리턴
    max = 0
    max_idx = S
    for idx, v in enumerate(visited):
        if max <= v:
            max, max_idx = v, idx
    print('#{} {}'.format(tc, max_idx))

    for i in range(101):
        if visited[i]:
            print(i, ':', visited[i])