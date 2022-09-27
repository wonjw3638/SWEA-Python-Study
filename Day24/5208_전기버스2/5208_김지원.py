# 5208 전기버스2
# 220927

'''
설계시간 14:31~32
구현시간 14:33~45
'''

import sys
sys.stdin = open('input.txt', 'r')

def drive(n, k, cnt):
    global answer

    if n >= N:
        if cnt < answer:
            answer = cnt
        return
    
    if cnt >= answer:
        return

    # 배터리 교체
    k = arr[n]

    for kk in range(k, 0, -1):
        # kk만큼 이동, kk만큼 소모
        drive(n+kk, k-kk, cnt+1)


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    answer = float('INF')

    # n번째 정류장에서 출발, 남은 배터리 용량, 교환 횟수(출발지점은 빼야하니까 -1)
    drive(1, 0, -1)

    print('#{} {}'.format(tc, answer))