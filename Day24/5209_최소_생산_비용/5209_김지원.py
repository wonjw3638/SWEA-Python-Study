# 5209 최소 생산 비용
# 220927

'''
설계시간 14:56~14:57 
구현시간 14:58~15:02
'''

# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

def produce(i, visited, cost):
    global answer

    if i == N:
        if cost < answer:
            answer = cost
        return
    
    if cost > answer:
        return
    
    for j in range(N):
        if visited[j] == 0:
            visit = visited[:]
            visit[j] = 1
            produce(i+1, visit, cost + arr[i][j])


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = float('INF')
    # 선택한 공장 표시
    choised = [0] * N
    
    # i번째 제품생산, 선택한 공장 리스트, 생산 비용
    produce(0, choised, 0)

    print('#{} {}'.format(tc, answer))