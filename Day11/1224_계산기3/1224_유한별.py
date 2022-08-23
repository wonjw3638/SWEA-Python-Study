# 1224_계산기2
# 2022-08-23

# 연산자에 맞는 연산 수행
def my_op(num1, num2, op):
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    return ops[op](int(num1), int(num2))


# 연산자 우선 순위
def primary(char):
    if char == '*' or char == '/': return 2
    elif char == '+' or char =='-': return 1
    else: return 0


# len 함수 구현
def my_len(arr):
    cnt = 0
    for _ in arr:
        cnt += 1
    return cnt

    
for tc in range(1, 11):
    N = int(input())
    exp = list(input())
    len_exp = my_len(exp)

    num_stack = []
    op_stack = []
    num_top = 0
    op_top = 0
    idx = 0
    
    print('#{}'.format(tc), end=' ')
    while idx < len_exp:
        # 괄호(열린) 처리
        if exp[idx] == '(':
            op_stack.append(exp[idx])
            op_top += 1
        # 괄호(닫힌) 처리
        elif exp[idx] == ')':
            # 괄호가 열린 위치 위에 쌓인 요소 모두 pop
            while op_top > 0:
                if op_stack[op_top-1] == '(':
                    op_stack.pop()
                    op_top -= 1
                    break
                else:
                    num_stack[num_top-2] = my_op(num_stack[num_top-2], num_stack.pop(), op_stack.pop())
                    num_top -= 1
                    op_top -= 1


        # 연산자가 나올 경우
        elif primary(exp[idx]):
            while op_top > 0:
                # 만약 top의 우선 순위가 현재 연산자보다 낮을 때
                if primary(op_stack[-1]) < primary(exp[idx]):
                    break
                # top 요소의 우선 순위가 현재 연산자보다 낮거나 같을 때
                else:
                    num_stack[num_top-2] = my_op(num_stack[num_top-2], num_stack.pop(), op_stack.pop())
                    num_top -= 1
                    op_top -= 1
            # 연산자 처리 후 새 요소 append
            op_stack.append(exp[idx])
            op_top += 1
        
        # 숫자가 나올 경우
        else:
            num_stack.append(int(exp[idx]))
            num_top += 1
            
        idx += 1
    
    # 나머지 연산자 처리
    while op_stack:
        num_stack[num_top-2] = my_op(num_stack[num_top-2], num_stack.pop(), op_stack.pop())
        num_top -= 1
        op_top -= 1
        
    print(num_stack[0])