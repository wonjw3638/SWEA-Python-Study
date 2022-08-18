# 4871_그래프 경로
# 220818
'''
설계 10:10 ~ 10:11
구현 10:11 ~ 10:30
'''
import sys
sys.stdin = open('input.txt','rt')

T = int(input())

def dfs(map_list, S, G, N):
    visited = [0] * N
    stack = [0] * N
    top = 0

    # 시작점 방문
    v = S
    visited[v] = 1
    stack[top] = v
    while True:
        for w in map_list[v]:
            # 도착점을 방문한 경우
            if w == G:
                visited[w] = 1
                return 1
            # 방문 안한 접점이 있는 경우
            if visited[w] == 0:
                top += 1
                visited[w] = 1
                stack[top] = w
                v = w
                break
            else:
                continue
        # 방문 안한 접점이 없는 경우
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break
    # 도착점 방문 안함
    if visited[G] == 0:
        return 0
    else:
        return 1


for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    N = V + 1
    map_list = [[] for _ in range(N)]
    # 경로 정보 입력
    for _ in range(E):
        s, d = list(map(int, input().split()))
        map_list[s].append(d)
    
    S, G = list(map(int, input().split()))
    answer = dfs(map_list, S, G, N)

    print('#{} {}'.format(tc, answer))