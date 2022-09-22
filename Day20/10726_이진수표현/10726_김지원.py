# 10726 이진수 표현
# 220920

'''
10:10 ~ 10:16
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    idx = 0
    answer = 'ON'
    while M and (idx < N):
        tmp = M%2
        if tmp == 0:
            answer = 'OFF'
            break
        else:
            M = M//2
            idx += 1
    if idx < N:
        answer = 'OFF'

    print('#{} {}'.format(tc, answer))