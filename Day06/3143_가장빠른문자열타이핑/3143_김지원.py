# 3143_가장 빠른 문자열 타이핑
# 220816
# 설계 10:01 ~ 10:01 - 1
# 구현 10:02 ~ 10:12 - 10

import sys
sys.stdin = open('input.txt','r')

T = int(input())

# 길이를 구하는 함수
def my_len(string):
    length = 0
    for _ in string:
        length += 1
    return length

def serch(A, B):
    M = my_len(A)
    N = my_len(B)
    idx = count = 0
    # 문자열 비교 시작
    for a in A:
        if idx == N-1:
            # 마지막 문자열까지 같은 경우
            if a == B[idx]:
                count += 1
                idx = 0
            else:
                # 다른데 첫 글자와 같은 경우    
                if a == B[0]:
                    idx = 1
                # 아예 다른 경우
                else:
                    idx = 0
        # 문자열과 같은 경우       
        if a == B[idx]:
            idx += 1
        else:
            # 다른데 첫 글자와 같은 경우    
            if a == B[0]:
                idx = 1
            # 아예 다른 경우
            else:
                idx = 0
    answer = (M - N * count) + count
    return answer


for tc in range(1, T+1):
    A, B = input().split()

    answer = serch(A, B)
    
    print('#{} {}'.format(tc, answer))