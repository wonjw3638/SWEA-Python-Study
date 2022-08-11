# 1966_숫자를 정렬하자
# 220811

import sys
sys.stdin = open('input.txt','r')

T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
 
    for i in range(N-1):
        minIdx = i     # 최소값 인덱스 
        for j in range(i+1, N):
            if numbers[minIdx] > numbers[j]: 
                minIdx = j     # 최소값 인덱스 업데이트
        numbers[i], numbers[minIdx] = numbers[minIdx] , numbers[i]    # 자리 바꾸기
     
    print('#{}'.format(tc), *numbers)