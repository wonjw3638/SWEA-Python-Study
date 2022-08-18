# 4866_괄호검사
# 220818
'''
설계 09:38 ~ 09:40
구현 09:40 ~ 09:45
'''

import sys
sys.stdin = open('input.txt','rt')

T = int(input())
dic = {
    ')' : '(',
    '}' : '{',
}
open_list = ['(', '{']

for tc in range(1, T + 1):
    string = input()
    stack = list()
    top = max_idx = -1
    answer = 1

    for s in string:
        if s in open_list:
            top += 1
            if top > max_idx:
                stack.append(s)
                max_idx += 1
            else:
                stack[top] = s
        elif s in dic:
            # 스택 마지막 값과 괄호가 제대로 된 짝인 경우
            if stack[top] == dic.get(s):
                stack[top] = ''
                top -= 1
            # 짝이 아닌 경우
            else:
                answer = 0
                break
    
    if answer == 1:
        for s in stack:
            if s != '':
                answer = 0
                break
        
    print('#{} {}'.format(tc, answer))