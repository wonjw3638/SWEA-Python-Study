# 9337_점점 커지는 당근의 개수
# 2022-08-12

#import sys
#sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    carrots = list(map(int, input().split()))

    max_cnt, cnt = 1, 1
    for i in range(1, N) : 
        if carrots[i-1] < carrots[i] : # 연속으로 커지는 당근 체크
            cnt += 1
        else :
            cnt = 1
        if cnt > max_cnt : # 맥스값 체크
            max_cnt = cnt

    print('#{} {}'.format(test_case, max_cnt))