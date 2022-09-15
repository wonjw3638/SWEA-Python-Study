# 4869_종이붙이기
# 220818
'''
설계 15m
구현 11:41~45  + 5

'''


import sys
sys.stdin = open('input.txt','rt')

T = int(input())

# 스택 생성
stack = [0] * 31
stack[1] = 1
stack[2] = 3
top = 2

for tc in range(1, T + 1):
    N = int(input())
    n = N//10
    if stack[n] == 0:
        for i in range(top, n):
            if stack[i+1] != 0:
                continue
            else:
                # 2 * 전전값 + 전값 메모이제션 사용
                stack[i+1] = (2 * stack[i-1]) + stack[i]

    print('#{} {}'.format(tc, stack[n]))