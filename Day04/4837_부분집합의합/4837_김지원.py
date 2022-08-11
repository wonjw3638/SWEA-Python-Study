# 4837_부분집합의 합
# 220811

import sys
sys.stdin = open('input.txt','r')

T = int(input())

def count(N, num):
    cnt = 0
    while num > 0 :
        cnt += num % 2  # 나머지 더하기
        num = num // 2

    if cnt == N:  # 1의 개수가 N개면 True
        return True
    else: 
        return False

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    answer = 0 

    for i in range(1<<12): # 전체 부분 집합 경우의 수
        sum_subset = 0
        if count(N, i):
            for j in range(12):
                if i & (1<<j):
                    sum_subset += (j + 1)  # 인덱스 + 1 = 값
            if sum_subset == K:
                answer += 1
        else:
            continue  # 부분집합의 원소 개수가 N개가 아니면 continue
        
    print('#{} {}'.format(tc, answer))