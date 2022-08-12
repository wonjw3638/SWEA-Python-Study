# 9386_연속한 1의 개수
# 2022-08-12

#import sys
#sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input()))
    max_cnt = 0
    cnt = 0
    while arr :
        num = arr.pop() # 순서의 상관이 없기 때문에 pop으로 처리, 다 튀어나오면 while문 종료

        if num : # 1이 연속으로 튀어나오는 중 일때
            cnt += num
        else : # 0이 튀어나올 때
            cnt = 0

        if max_cnt < cnt : # 만약 연속된 1이 max보다 크면 바꿔주기
            max_cnt = cnt

    print ('#{} {}'.format(test_case, max_cnt))