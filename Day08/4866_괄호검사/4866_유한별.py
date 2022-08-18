# 4866_괄호검사
# 2022-08-18

T = int(input())

for tc in range(1, T+1) :
    input_str = input()
    stack = []
    flag = 1
    brakets = ['{', '}', '(', ')']
    # 1글자씩 확인
    for char in input_str :
        if char in brakets :
            # stack에 1개라도 요소가 들어가 있으면 검사
            if stack :
                # 만약 짝이 맞는 괄호가 나올 경우 스택에서 삭제
                # 시작하는 괄호 (, { 가 나왔을 경우 스택에 push
                if stack[-1] == '(' :
                    if char == ')' : 
                        stack.pop()
                    elif char == '}' :
                        flag = 0
                        break
                    else :
                        stack.append(char)
                        
                elif stack[-1] == '{' :
                    if char == '}' : 
                        stack.pop()
                    elif char == ')' :
                        flag = 0
                        break
                    else :
                        stack.append(char)

            # 스택이 비었을 경우
            # 만약 닫히는 괄호가 들어올 경우 0 출력
            else :
                if char == '}' or char == ')' :
                    flag = 0
                    break
                stack.append(char)
    
    # 모든 과정을 처리했는데 stack에 요소가 남아있을 경우(짝이 완전히 안지어지면)
    if stack :
        flag = 0
    print('#{} {}'.format(tc, flag))