# 1209_Sum
# 2022-08-10

# import sys
# sys.stdin = open('input.txt','r')

for _ in range(10) :
    test_case = int(input())
    matrix = []
    max_sum = 0

    for i in range(100) :
        matrix.append(list(map(int, input().split())))
    
    sum_diag_up, sum_diag_down = 0, 0
    for i in range(100) :
        sum_row = 0
        sum_col = 0
        for j in range(100) :
            sum_row += matrix[i][j] # i번째 행의 합
            sum_col += matrix[j][i] # i번째 열의 합
        if max_sum < sum_row : 
            max_sum = sum_row
        if max_sum < sum_col :
            max_sum = sum_col
        sum_diag_up += matrix[i][99-i] # 우상향 대각선의 합
        sum_diag_down += matrix[i][i] # 우하향 대각선의 합

    if max_sum < sum_diag_up :
        max_sum = sum_diag_up
    if max_sum < sum_diag_down :
        max_sum = sum_diag_down

    # 그 중의 max 출력
    print('#{} {}'.format(test_case, max_sum))