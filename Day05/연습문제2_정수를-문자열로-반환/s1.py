# 연습문제2 - 정수를 문자열로 반환
# 220812

import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 7):
    N = int(input())

    flag = ''     # 음수일 경우 부호
    answer = ''   # 정답 문자열

    if N < 0:     # 음수면 앞에 -기호 붙여줌
        flag = '-'
        N = N * (-1)
    elif N == 0:       # 0이면 while문 x
        answer = '0'

    while N:
        N, remainder = N//10, N%10    # 뒤에서부터 나머지를 더해가면서
        answer = str(remainder) + answer
    
    print('#{} {}'.format(tc, flag + answer))