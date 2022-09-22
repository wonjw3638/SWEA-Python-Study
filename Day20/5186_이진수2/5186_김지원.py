# 5816 이진수2
# 220920

'''
09:53~10:07
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    num = float(input())
    answer = ''
    while num:
        num = num * 2
        if num >= 1:
            answer += '1'
            num -= 1
        else:
            answer += '0'
        
        if len(answer) > 12:
            answer = 'overflow'
            break
    
    print('#{} {}'.format(tc, answer))