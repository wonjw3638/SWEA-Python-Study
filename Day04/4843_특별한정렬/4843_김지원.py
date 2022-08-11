# 4843_특별한정렬
# 220811

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    for i in range(10):  # 어차피 10개만 출력할거니까 앞의 10개까지만 정렬
        if i%2 : # index 홀수 -> min 구하기
            minIdx = i
            for j in range(i+1, N):
                if num_list[minIdx] > num_list[j] :
                        minIdx = j
            num_list[i], num_list[minIdx] = num_list[minIdx], num_list[i]
        else:   # index 짝수 -> max 구하기
            maxIdx = i
            for j in range(i+1, N):
                if num_list[maxIdx] < num_list[j] :
                        maxIdx = j
            num_list[i], num_list[maxIdx] = num_list[maxIdx], num_list[i]

    print('#{}'.format(tc), end = ' ')
    for idx in range(10):
        print(num_list[idx], end = ' ')
    print()