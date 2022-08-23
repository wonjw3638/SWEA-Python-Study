# 4881_배열최소합
# 220823
'''
설계 09:58~10:07
구현 10:08~11:34
'''

import sys
sys.stdin = open('input.txt','rt')

T = int(input())

def permutation(i, N):
    global answer
    tmp = 0
    # 순열 완성
    if i == N:
        for n in range(N):
            tmp += arr[n][N_list[n]]
            if tmp >= answer:
                break
        else:
            answer = tmp
    else:
        # N_list[0:i] 까지의 합이 이미 최솟값을 초과하면 고려하지 않을 예정.
        for idx in range(i):
            tmp += arr[idx][N_list[idx]]
            # 최솟값 초과한경우
            if tmp >= answer:
                break
        else:
            for j in range(i, N):
                N_list[i], N_list[j] = N_list[j], N_list[i]
                permutation(i+1, N)
                N_list[i], N_list[j] = N_list[j], N_list[i]


for tc in range(1, T+1):
    N = int(input())
    N_list = [ i for i in range(N)]

    arr = list()
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 초기값을 가장 큰 값으로 설정
    answer = 987654321
    permutation(0, N)
    
    print('#{} {}'.format(tc, answer))