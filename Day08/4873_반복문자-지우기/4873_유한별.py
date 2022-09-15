# 4873_반복문자 지우기
# 2022-08-18

T = int(input())

for tc in range(1, T+1) :
    input_str = input()
    stack = []
    n = 0
    # 1글자씩 확인
    for char in input_str :
        # stack에 1개라도 요소가 들어가 있으면 검사
        if stack :
            # 만약 동일한 문자가 나올 경우 스택에서 삭제
            if stack[-1] == char :
                n -= 1
                stack.pop()
            else :
                n += 1
                stack.append(char)            
        # 스택이 비었을 경우
        else :
            n += 1
            stack.append(char)
        
    print('#{} {}'.format(tc, n))