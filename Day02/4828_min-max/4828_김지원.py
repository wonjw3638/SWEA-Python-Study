# 4828_min-max
# 220809

import sys
sys.stdin = open('input.txt','r')

N = int(input())

for tc in range(1, N+1):
    min, max = 987654321, -1
    T = input()
    numbers = list(map(int, input().split()))

    for num in numbers:
        if num >= max:
            max = num
        if num <= min :
            min = num

    print('#{} {}'.format(tc, max - min))