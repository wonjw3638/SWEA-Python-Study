# 5189 전자카트
# 220922

'''
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 순열 구하기
def f(i, k):
    if i == k:
        tmp = num[::]
        # 카트의 경로 => 1에서 시작, 1에서 끝남
        result.append(([1] + tmp + [1]))
    else:
        for j in range(i, k):
            num[i], num[j] = num[j], num[i]
            f(i+1, k)
            num[i], num[j] = num[j], num[i]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = [i for i in range(2, N+1)]

    # 순열구하기
    result = list()
    f(0, N-1)

    answer = 987654321
    for per in result:
        tmp = 0
        for idx in range(len(per)-1):
            tmp += arr[per[idx]-1][per[idx+1]-1]
            if tmp >= answer:
                break
        else:
            answer = tmp

    print('#{} {}'.format(tc, answer))