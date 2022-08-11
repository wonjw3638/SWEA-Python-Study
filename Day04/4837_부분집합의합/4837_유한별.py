# 4837_부분집합의 합 풀이
# 2022-08-11 

# import sys
# sys.stdin = open('input.txt','r')

T = int(input())
A_set = [i for i in range(1, 13)]

for test_case in range(1, T+1) :
    N, K = map(int, input().split())

    is_true = 0
    for i in range(1<<12) :     # 2^12만큼 반복(000000000000 ~ 111111111111)
        cnt = 0
        sum_subset = 0
        for j in range(12) :    # 1을 하나씩 밀어가며 비교 (000000000001 000000000010 000000000100 ...)
            if i & (1<<j) :     # i에 j를 가졌을때(j번째 idx를 subset의 element로 가질 때)
                cnt += 1        # cnt는 부분집합의 크기(elements의 개수) 
                sum_subset += A_set[j - 1] # sum_subset은 부분집합 원소들의 합
        if cnt == N and sum_subset == K :
            is_true += 1        # 조건 만족 때마다 count
    
    print('#{} {}'.format(test_case, is_true))