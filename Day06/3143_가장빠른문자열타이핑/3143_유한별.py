# 3143_가장빠른문자열타이핑
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
    A, B = map(list, input().split())
    idx = 0
    n = my_len(A)
    m = my_len(B)
    cnt = 0

    # A 문자열 끝까지 탐색
    while idx < n :
        # B 가 A 안에 있는지 확인
        if A[idx] == B[0] :
            # 인덱스를 벗어날 경우 & 없을 경우
            for i in range(m) :
                if idx + i == n :
                    break
                if A[idx + i] != B[i] :
                    break
            # 있을 경우
            else :
                idx += m - 1
        cnt += 1
        idx += 1

    print('#{} {}'.format(test_case, cnt))