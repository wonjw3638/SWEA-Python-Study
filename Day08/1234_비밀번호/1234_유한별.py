# 1234_비밀번호
# 2022-08-18

# 사실상 4873과 완전히 같은 문제
for tc in range(1, 11) :
    n, input_str = input().split()
    stack = []
    # 1글자씩 확인
    for char in input_str :
        # stack에 1개라도 요소가 들어가 있으면 검사
        if stack :
            # 만약 동일한 문자가 나올 경우 스택에서 삭제
            if stack[-1] == char :
                stack.pop()
            else :
                stack.append(char)            
        # 스택이 비었을 경우
        else :
            stack.append(char)
        
    print('#{} {}'.format(tc, ''.join(stack)))