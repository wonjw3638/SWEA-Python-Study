# 4874_Stack2
# 2022-08-23

# 연산자에 맞는 연산 수행
def my_op(num1, num2, op):
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }
    return ops[op](int(num1), int(num2))


def my_len(my_arr):
    cnt = 0
    for _ in my_arr:
        cnt += 1
    return cnt


T = int(input())
operator = ['+', '-', '*', '/']

for tc in range(1, T+1):
    arr = list(input().split())
    n = my_len(arr)
    stack = []
    top = 0
    error = False
    
    print('#{}'.format(tc), end=' ')

    for element in arr:
        if element in operator:
            if top < 2:
                error = True
                break
            else:
                stack[top-2] = my_op(stack[top-2], stack.pop(), element)
                top -= 1
        elif element == '.':
            break
        else:
            stack.append(int(element))
            top += 1
    
    if top > 1 or error:
        print('error')
    else:
        print(stack[0])