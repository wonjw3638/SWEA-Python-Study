# 1974_스도쿠검증
# 2022-08-16

# row 검사
def check_row(table) :
    for i in range(9) :
        # 1-9까지 각 숫자의 개수를 세는 list 생성
        check = [0 for j in range(10)]
        return_value = 1
        for j in range(9) :
            # 한 row 내의 중복 확인
            if check[table[i][j]] == 0 :
                check[table[i][j]] += 1
            else :
                return_value = 0
                break
        if return_value == 0 :
            break
    # 중복이 한번도 발생하지 않을 경우
    return return_value


# col 검사
def check_col(table) :
    for i in range(9) :
        # 1-9까지 각 숫자의 개수를 세는 list 생성
        check = [0 for j in range(10)]
        return_value = 1
        for j in range(9) :
            # 한 col 내의 중복 확인
            if check[table[j][i]] == 0 :
                check[table[j][i]] += 1
            else :
                return_value = 0
                break
        if return_value == 0 :
            break
    # 중복이 한번도 발생하지 않을 경우
    return return_value


def check_sqr(table) :
    # i,j 는 각 3*3칸의 좌측 꼭지점 좌표
    for i in [0, 3, 6] :
        for j in [0, 3, 6] :
            # 1-9까지 각 숫자의 개수를 세는 list 생성
            check = [0 for k in range(10)]
            return_value = 1
            # 3*3칸 내의 중복 확인
            for k in range(3) :
                for l in range(3) :
                    if check[table[i+k][j+l]] == 0 :
                       check[table[i+k][j+l]] += 1
                    else :
                        return_value = 0
            if return_value == 0 :
                break
        if return_value == 0 :
            break
    # 중복이 한번도 발생하지 않을 경우
    return return_value


T = int(input())

for test_case in range(1, T + 1) :
    table = [[0 for i in range(9)] for j in range(9)]
    
    for i in range(9) :
        table[i] = list(map(int, input().split()))
    
    print(f'#{test_case}', end=' ')
    # row, col, square 모두 중복이 없어야만 1 출력
    if check_row(table) == 1 and check_col(table) == 1 and check_sqr(table) == 1 :
        print(1)
    else : print(0)