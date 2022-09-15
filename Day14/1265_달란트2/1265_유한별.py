# 1265_달란트 문제풀이
# 2022-08-26

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    d = N // P
    result = 1
    for _ in range(N-d*P):
        result *= (d+1)
    for _ in range(P-(N-d*P)):
        result *= d
    print('#{} {}'.format(tc, result))