import random
import sys

sys.stdin = open('input.txt', 'r')
# T = int(input()) # 가장 첫줄

# 함수는 for문 위에다 작성

for tc in range(1, 10+1) :
    T = int(input())
    col = list(map(int, input().split()))
    answer = 0
    for i in range(2, T-2) :
        if col[i] > col[i-2] and col[i] > col[i-1] and col[i] > col[i+1] and col[i] > col[i+2] : # 가운데 기준 좌 우 2개씩 비교
            sech = col[i-2] 
            for j in [col[i-1], col[i+1], col[i+2]]: # 가운데가 가장 크면 두번째 높이 구하기
                if sech < j :
                    sech = j
            answer += col[i] - sech # 기둥의 높이차만큼 쌓기


    print('#{} {}' .format(tc,answer))