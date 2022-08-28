# 5099_피자 굽기
# 220826
'''
설계 21:40 ~ 21:45
구현 23:25 ~ 23:48
'''

import sys
sys.stdin = open('input.txt','rt')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    Ci = list(map(int, input().split()))
    pizza = list()

    for m, c in enumerate(Ci):
        pizza.append([c, m+1])

    queue = [0] * N
    rear = idx = -1
    for _ in range(N):
        rear = ( rear + 1 ) % N
        idx += 1
        queue[rear] = pizza[idx]

    while True:

        rear = ( rear + 1 ) % N
        # 비어있는 곳인 경우 개수 세기
        if queue[rear] == 0:
            if cnt == N:
                break
            cnt += 1
            continue
        else:
            cnt = 0

        # 치즈의 양이 0일 때
        if queue[rear][0] // 2 == 0:
            # 남은 피자가 있는 경우
            idx += 1
            if idx < M :
                queue[rear] = pizza[idx]
            else:
                answer = queue[rear][1]
                queue[rear] = 0
        # 치즈의 양이 0이 아닐 때
        else:
            queue[rear] = [queue[rear][0] // 2, queue[rear][1]]
    
    print('#{} {}'.format(tc, answer))
