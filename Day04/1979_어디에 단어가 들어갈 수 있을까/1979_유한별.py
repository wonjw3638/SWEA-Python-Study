# 1979_어디에 단어가 들어갈 수 있을까
# 2022-08-11 

# import sys
# sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = []

    for i in range(n) :
        puzzle.append(list(map(int, input().split())))

    count = 0
    count_row = 0
    count_col = 0

    for i in range(n) :
        check_row = [] # 가로를 검사할 check_row라는 새로운 list 생성
        check_col = [] # 세로를 검사할 check_col이라는 새로운 list 생성

        for j in range(n) :
            if j == 0 :
                check_row.append(puzzle[i][j]) # 왼쪽 벽에서 시작할 경우
                check_col.append(puzzle[j][i]) # 위쪽 벽에서 시작할 경우
            else :
                if puzzle[i][j] == 0 : # 가로축 검사 : 만약 현재 idx에 들어있는 값이 0이라면 넘어감
                    check_row.append(0)
                else : # idx의 값이 0이 아니라면(1로 그려져 있다면) 몇개 연속하는지 확인할거임
                    check_row.append(check_row[j-1] + puzzle[i][j]) # 연속된 개수를 적어줌
                    check_row[j-1] = 0 # 기존의 것은 지움(중복 방지! ex : 5개 안에 3개가 있는 걸 셀까봐)

                if puzzle[j][i] == 0 : # 세로축 검사
                    check_col.append(0)
                else :
                    check_col.append(check_col[j-1] + puzzle[j][i])
                    check_col[j-1] = 0

        for j in range(n) :
            if check_row[j] == k : # 1이 가로로 k개 연속된게 있다면
                count_row += 1
            if check_col[j] == k : # 1이 세로로 k개 연속된게 있다면
                count_col += 1
    count = count_row + count_col # 총 합
    print(f'#{test_case}', count)