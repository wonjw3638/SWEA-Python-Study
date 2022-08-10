import sys
sys.stdin = open('input.txt','r')

for he in range(1, 10+1) :
    test = int(input())
    square = [list(map(int, input().split())) for _ in range(100)]
    maxlr = 0
    maxrl = 0
    maxcol = 0
    maxcol = 0
    maxrow = 0
    for i in range(100) :
        sumrow = 0
        for j in range(100) :
            sumrow += square[i][j] # 행의 합 구하기
            if maxrow <= sumrow :
                maxrow = sumrow # 행의 합 최대 구하기

    for j in range(100) :
        sumcol = 0
        for i in range(100) :
            sumcol += square[i][j] # 열의 합 구하기
            if maxcol <= sumcol :
                maxcol = sumcol # 열의 합 최대 구하기

    for i in range(100) : 
        for j in range(100) :
            if i == j :
                maxlr += square[i][j] # 좌우 대각
    for i in range(100) : 
        for j in range(100) :
            if i + j == 99 :
                maxrl += square[i][j] # 우좌 대각


    if maxrl >= maxlr and maxrl >= maxcol and maxrl >= maxrow:
        print(f'#{he} {maxrl}')        
    elif maxlr >= maxrl and maxlr >= maxrow and maxlr >= maxcol :
        print(f'#{he} {maxlr}')
    elif maxrow >= maxlr and maxrow >= maxcol and maxrow >=maxrl :
        print(f'#{he} {maxrow}')        
    elif maxcol >= maxlr and maxcol >= maxrl and  maxcol >= maxlr:
        print(f'#{he} {maxcol}')