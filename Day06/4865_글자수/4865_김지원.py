# 4865_글자수
# 220816
# 설계 09:53 ~ 09:55 - 2
# 구현 09:55 ~ 09:57 - 2

import sys
sys.stdin = open('input.txt','r')

T = int(input())


for tc in range(1, T+1):
    # 중복 제거
    str1 = set(input())
    str2 = input()

    # 글자 수를 셀 딕셔너리 생성
    string = {s:0 for s in str1}
    
    # 글자가 딕셔너리에 존재하면 - 1씩 증가하면서 개수 세기
    for s in str2:
        if s in string:
            string[s] += 1
    
    answer = -1
    # 딕셔너리 순회, 글자 개수가 가장 큰 값 반환
    for key, value in string.items():
        if value > answer:
            answer = value

    print('#{} {}'.format(tc, answer))