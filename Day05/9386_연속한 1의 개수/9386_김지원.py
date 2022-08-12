# 9386 - 연속한 1의 개수
# 220812

import sys
sys.stdin = open('input.txt','rt', encoding='UTF8')

T = int(input())

for tc in range(1, T + 1):
    lenString = int(input())
    string = input()
    maxOne = cnt = 0
    for s in string:
        if s == '1':  # string 값이 1이면 개수 세어나감
            cnt += 1
            if cnt > maxOne:  # 개수가 최대 개수값 보다 크면 값 업데이트
                maxOne = cnt
        else:
            cnt = 0
    
    print('#{} {}'.format(tc, maxOne))