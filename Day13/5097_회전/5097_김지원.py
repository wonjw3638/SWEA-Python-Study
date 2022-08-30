# 5907_회전
# 220826
'''
설계 02:50~02:51
구현 02:51~02:52
'''

import sys
sys.stdin = open('input.txt','rt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    idx = M % N

    print('#{} {}'.format(tc, numbers[idx]))