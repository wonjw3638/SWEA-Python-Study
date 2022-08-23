# 4874_Forth
# 220823
'''
설계 09:13~09:15
구현 09:16~09:48
'''
import sys
sys.stdin = open('input.txt','rt')

operator = ['+', '-', '*', '/', '.']
T = int(input())

for tc in range(1, T+1):
    try:
        N = list(input().split())
        stack = [0] * 256
        top = -1
        answer = num = opt = 0

        # 수식 문자열 읽기
        for n in N:
            # 피연산자인 경우
            if not (n in operator):
                top += 1
                num += 1
                stack[top] = int(n)
            # 연산자인 경우
            else:
                opt += 1
                if n == '+':
                    tmp = stack[top] + stack[top-1]
                    stack[top] = stack[top-1] = 0
                    top -= 1
                    stack[top] = tmp

                elif n == '-':
                    tmp = stack[top - 1] - stack[top]
                    stack[top] = stack[top-1] = 0
                    top -= 1
                    stack[top] = tmp

                elif n == '*':
                    tmp = stack[top] * stack[top-1]
                    stack[top] = stack[top-1] = 0
                    top -= 1
                    stack[top] = tmp
                    
                elif n == '/':
                    tmp = stack[top - 1] // stack[top]
                    stack[top] = stack[top-1] = 0
                    top -= 1
                    stack[top] = tmp
                # '.'인 경우
                else:
                    if (opt == num) :
                        answer = stack[top]
                        break
                    # 오류 내기
                    else:
                        1//0
        print('#{} {}'.format(tc, answer))
    # 오류가 났을 때 
    except:  
        print('#{} error'.format(tc))