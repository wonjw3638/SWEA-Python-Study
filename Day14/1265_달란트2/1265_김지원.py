# 1265_달란트
# 220913

import sys
sys.stdin = open('input.txt','rt')

T = int(input())

for tc in range(1, T+1):
    N , P = list(map(int, input().split()))
    # 한묶음당 최소로 들어가야 하는 갯수
    quot = N // P
    rem = quot + 1
    n = 0

    # 나누어 떨어지는 경우
    if not N % P :
        answer = quot**P
    # 나누어 떨어지지 않는 경우 한 묶음에 하나씩 더해가면서 값 찾기
    else:
        while True:
            n += 1
            if (quot * (P-n)) + (rem * n) == N:
                answer = (quot**(P-n)) * ((rem)**n)
                break

    print('#{} {}'.format(tc, answer))