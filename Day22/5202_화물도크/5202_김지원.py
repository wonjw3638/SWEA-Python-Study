# 5202 화물 도크
# 220922

'''
10분?
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    trucks = [list(map(int, input().split())) for _ in range(N)]
    # 작업 종료 시간, 시작 시간을 기준으로 정렬
    trucks.sort(key = lambda x : (x[1], x[0]))

    tmp = trucks[0][1]
    cnt = 1

    # 시작 시간이 종료시간보다 같거나 크면 카운트 세고 그 트럭 선택
    for truck in trucks[1:]:
        if truck[0] >= tmp:
            cnt += 1
            tmp = truck[1]

    print('#{} {}'.format(tc, cnt))