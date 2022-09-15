# 4864_문자열 비교
# 220816
# 설계 09:34~09:35 - 1
# 구현 09:35~09:49 - 14

import sys
sys.stdin = open('input.txt','r')

T = int(input())

# 길이를 구하는 함수
def my_len(string):
    length = 0
    for _ in string:
        length += 1
    return length

# 문자열 검색하는 함수
def serch(str1, str2):
    N = my_len(str1)
    idx = 0
    for s2 in str2:
        # str1의 마지막값까지 같은 경우 1 반환
        if idx == N-1:
            if s2 == str1[idx]:
                return 1
        # str1 idx번째 값과 값이 같은 경우
        if s2 == str1[idx]:
            idx += 1
        # str1의 idx번째 값과 같지 않은 경우
        else: 
            idx = 0
            # str1 0번째 값과 값이 같은 경우
            if s2 == str1[idx]:
                idx += 1
    # 같은 문자열이 하나도 없는 경우
    return 0

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    answer = serch(str1, str2)

    print('#{} {}'.format(tc, answer))