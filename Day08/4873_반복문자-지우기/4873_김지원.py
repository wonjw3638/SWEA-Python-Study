# 4873_반복문자 지우기
# 220818
'''
설계 09:17 ~ 09:19 - 2
구현 09:20 ~ 09:34 - 14
'''

import sys
sys.stdin = open('input.txt','rt')

T = int(input())

for tc in range(1, T + 1):
    string = input()
    stack = [string[0]]
    top = max_idx = 0
    for s in string[1:]:
        # stack 마지막 값과 같은 경우
        if stack[top] == s:
            stack[top] = ''
            top -= 1
        # stack 마지막 값과 다른 경우
        else:
            top += 1
            if top > max_idx:
                stack.append(s)
                max_idx += 1
            else:
                stack[top] = s
    print('#{} {}'.format(tc, top + 1))
