import sys
sys.stdin = open('input.txt','r')
for he in range(1,11) :
    a=int(input())
    pan = []
    for i in range(100):
        pan.append(input())
    my_max = 0
    # 가로 행만 검색하기 위해 i를 찾고 j와 k를 이용해 범위 주기
    for i in range(100):
        for j in range(100):
            for k in range(100):
                # 리스트의 길이가 100이므로 j+k가 100을 넘어가지 않게 조건달기
                if j+k >=0 and j+k <=100 :
                    # 가로행이 범위 안에서 회문인지 판단
                    if pan[i][j:j+k]==pan[i][j:j+k][::-1] :
                        # 회문의 길이 판단
                        if my_max < k :
                            my_max = k
                            # print(i, j, k)
                            # print(pan[i][j:j+k])
    for i in range(100):
        col = []
        for j in range(100):
        # 세로열만 모인 리스트 col 생성
            col.append(pan[j][i])
        for j in range(100):
            for k in range(100):       
                if j+k >=0 and j+k <=100 :
                    # 세로열이 범위 안에서 회문인지 판단
                    if col[j:j+k]==col[j:j+k][::-1] :
                        # 회문의 길이 판단
                        if my_max < k :
                            my_max = k
    print('#{} {}'.format(he, my_max))




