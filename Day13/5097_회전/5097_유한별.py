# 5097_회전
# 2022-08-25

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    M %= N
    print('#{} {}'.format(tc, arr[M]))