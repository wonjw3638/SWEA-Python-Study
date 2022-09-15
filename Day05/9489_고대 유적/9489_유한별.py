# 9489_고대유적
# 2022-08-12

#import sys
#sys.stdin = open('input.txt','r')

def compare(a, b) : # 두 값을 비교해 큰 값 return
    if a > b :
        return a
    else :
        return b


def check_col(table, j, n) : # 열(세로)에서 max 길이 찾아 return
    max_cnt = cnt = 0

    for i in range(n) :
        cnt = cnt + 1 if table[i][j] else 0
        max_cnt = compare(max_cnt, cnt)
    
    return max_cnt


def check_row(table, i, m) : # 행(가로)에서 max 길이 찾아 return
    max_cnt = cnt = 0

    for j in range(m) :
        cnt = cnt + 1 if table[i][j] else 0
        max_cnt = compare(max_cnt, cnt)
    
    return max_cnt


T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    table = []
    max_cnt = 0

    for i in range(N) :
        table.append(list(map(int, input().split()))) # 한 줄씩 입력 받기
        max_cnt = compare(max_cnt, check_row(table, i, M)) # 받는 김에 check_row 돌리기

    for j in range(M) :
        max_cnt = compare(max_cnt, check_col(table, j, N)) # check_col 돌리기
    
    print('#{} {}'.format(test_case, max_cnt))