# 1219_길찾기
# 220818
'''
설계 10:47 ~ 10:49
구현 11:00 ~ 11:17
'''
import sys
sys.stdin = open('input.txt','rt')

# DFS 함수 구현
def dfs(map_list):
    visited = [0] * 100
    stack = [0] * 100
    top = 0

    visited[0] = 1
    stack[top] = 1
    v = 0
    while True:
        for w in map_list[v]:
            # 도착지점 방문 - 1반환, 함수종료
            if w == 99:
                visited[w] = 1
                return 1
            if visited[w] == 0:
                visited[w] = 1
                top += 1
                stack[top] = w
                v = w
                break
        else:
            if top == -1:
                break
            else:
                top -= 1
                v = stack[top]

for _ in range(10):
    tc, E = list(map(int, input().split()))
    info = list(map(int, input().split()))
    map_list = [[] for _ in range(100)]
    # 2차원 리스트에 경로 정보 저장
    for i in range(0, 2 * E, 2):
        map_list[info[i]].append(info[i + 1])
    answer = dfs(map_list)
    print('#{} {}'.format(tc, answer))

