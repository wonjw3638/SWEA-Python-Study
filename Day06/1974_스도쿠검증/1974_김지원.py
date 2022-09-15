# 1974_스도쿠 검증
# 220816

import sys
sys.stdin = open('input.txt','r')

T = int(input())

# 중복 검사 함수
def check(sudoku):
    tmp = list()
    # 행 검사
    for i in range(9):
        for j in range(9):
            # 중복인 경우
            if sudoku[i][j] in tmp:
                return 0
            tmp.append(sudoku[i][j])
        tmp.clear()

    # 열 검사
    for j in range(9):
        for i in range(9):
            # 중복인 경우
            if sudoku[i][j] in tmp:
                return 0
            tmp.append(sudoku[i][j])
        tmp.clear()
    
    # 칸 검사
    d = [0, 3, 6]
    for di in d:
        for dj in d:
            for i in range(3):
                for j in range(3):
                    # 중복인 경우
                    if sudoku[i + di][j + dj] in tmp:
                        return 0
                    tmp.append(sudoku[i + di][j + dj])
            tmp.clear()
    return 1

for tc in range(1, T + 1):
    sudoku = list()
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    answer = check(sudoku)

    print('#{} {}'.format(tc, answer))