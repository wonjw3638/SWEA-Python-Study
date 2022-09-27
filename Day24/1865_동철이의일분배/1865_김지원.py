# 1865 동철이의 일분배
# 220927

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

divide = lambda x : x/100

# n번째 사람, visited
def distrib(n, visit, ans):
    global answer

    # 최종값이 더 크면 답 update
    if n == N:
        if ans > answer:
            answer = ans
        return
    
    # 앞으로 곱해지는 수는 다 1보다 작으니까 중간에 멈춰주기
    if ans < answer:
        return

    for idx in range(N):
        if visit[idx] == 0:
            # 일 성공할 확률이 0이면 그냥 넘기기
            if arr[n][idx] == 0:
                continue
            visited = visit[:]
            visited[idx] = 1
            distrib(n+1, visited, ans*arr[n][idx])

    return

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(divide, list(map(int, input().split())))) for _ in range(N)]
    answer = 0
    visit = [0] * N
    
    # 1번째 사람부터 
    distrib(0, visit, 100)

    print('#{} {}'.format(tc, format(answer,".6f")))