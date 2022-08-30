# 5102_노드의 거리
# 220826

'''
설계 01:21~01:24
구현 01:25~01:40
'''

import sys
sys.stdin = open('input.txt','rt')

# BFS 구현
def bfs(S, G):
    visited = [0] * (V + 1)
    queue = [0] * (V + 1)
    rear = front = -1

    v = S
    visited[v] = 1
    rear += 1
    queue[rear] = v

    # 큐가 비어있으면 멈춤
    while front < rear :
        
        front += 1
        v = queue[front]

        # 이어진 노드로 이동
        for w in map_list[v]:
            if w == G:
                return visited[v]

            if visited[w] == 0:
                visited[w] = visited[v] + 1
                rear += 1
                queue[rear] = w
            else:
                continue
    
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    map_list = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = list(map(int, input().split()))
        map_list[a].append(b)
        map_list[b].append(a)

    S, G = list(map(int, input().split()))
    
    answer = bfs(S, G)



    print('#{} {}'.format(tc, answer))