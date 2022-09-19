# 2001_파리 퇴치
# 2022-08-11 

# import sys
# sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1) :
    n, m = map(int, input().split())

    table = []
    for _ in range(n) :
        table.append(list(map(int, input().split())))

    max_cnt = 0
    for i in range(n-m+1) : # 왼쪽 위 모서리의 row값
        for j in range(n-m+1) : # 왼쪽 위 모서리의 col값
            cnt = 0
            for k in range(m) : # m * m 사이즈로 체크
                for l in range(m) :
                    cnt += table[i+k][j+l]
            if max_cnt < cnt : # max값 찾기~
                max_cnt = cnt
    
    print('#{}'.format(test_case), max_cnt)