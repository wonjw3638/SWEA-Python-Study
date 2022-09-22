# 5201 컨테이너 운반
# 220922

'''
14:47~14:57
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))

    # 화물, 트럭 큰거부터 정렬
    cont = list(map(int, input().split()))
    cont.sort(reverse=True)
    trucks = list(map(int, input().split()))
    trucks.sort(reverse=True)

    # 가장 큰 화물부터 운반
    idx = answer = 0
    for truck in trucks:
        if idx > N-1: break
        if cont[idx] <= truck:
            answer += cont[idx]
            idx += 1
        else:
            idx += 1
            while idx < N:
                if cont[idx] <= truck:
                    answer += cont[idx]
                    idx += 1
                    break
                else:
                    idx += 1
                    continue

    print('#{} {}'.format(tc, answer))