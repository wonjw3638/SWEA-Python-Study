# 5356_의석이의 세로로 말해요
# 220816

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    # 문자열 최대 길이
    string = [''] * 15
    for _ in range(5):
        input_string = input()
        # 문자열을 하나씩 세로로 받음
        for idx, s in enumerate(input_string):
            string[idx] += s

    answer = ''
    for ans in string:
        answer += ans

    print('#{} {}'.format(tc, answer))