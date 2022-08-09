# 4835_구간합
# 220809

import sys
sys.stdin = open('input.txt','r')

def my_sum(li):
    ans = 0
    for i in li:
        ans += i
    return ans

N = int(input())

for tc in range(1, N+1):
    min, max, tmp = 987654321, 0, 0
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    for idx in range(N-M+1):
        tmp = my_sum(numbers[idx:idx+M])
        if tmp >= max:
            max = tmp
        if tmp <= min :
            min = tmp

    print('#{} {}'.format(tc, max - min))