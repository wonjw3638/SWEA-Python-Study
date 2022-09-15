# 4834_숫자카드
# 220809

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T+1):
    N = input()
    cnt = [0] * 10
    numbers = list(map(int, list(input())))

    for n in numbers:
        cnt[n] += 1

    max, idx = 0, 0
    for i, num in enumerate(cnt):
        if num >= max:
            idx = i
            max = num

    print('#{} {} {}'.format(tc, idx, max))