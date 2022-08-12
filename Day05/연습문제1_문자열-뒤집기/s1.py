# 연습문제1 - 문자열 뒤집기
# 220812

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T+1):

    string = input()
    answer = string[::-1]

    print('#{} {}'.format(tc, answer))