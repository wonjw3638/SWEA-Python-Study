# 4864_문자열 비교
# 2022-08-16

#import sys
#sys.stdin = open('input.txt','r')

# 내장함수 len 대체
def my_len(arr) :
    cnt = 0
    for a in arr :
        cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T+1) :
    # 각 string을 list로 변환하여 입력 받음
    A = list(input())
    B = list(input())
    n = my_len(A)
    m = my_len(B)
    idx = 0
    flag = 0
    
    # B 문자열 끝까지 탐색
    while idx < m :
        # B안에 A가 있는지 확인
        if B[idx] == A[0] :
            # 인덱스를 벗어날 경우 & 없을 경우
            for i in range(n) :
                if idx + i == m :
                    break
                if B[idx + i] != A[i] :
                    break
            # 있을 경우
            else :
                flag = 1
                idx += m - 1
        idx += 1
    
    print('#{} {}'.format(test_case, flag))