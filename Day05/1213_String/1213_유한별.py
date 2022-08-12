# 1213_string
# 2022-08-12

# import sys
# sys.stdin = open('input.txt','r')

def my_len(my_str) : # len 함수 구현
    cnt = 0
    for c in my_str :
        cnt += 1
    return cnt

for _ in range(10) :
    test_case = int(input())
    to_find = input()
    my_str = input()

    n = my_len(my_str)
    m = my_len(to_find)
    cnt = 0

    for i in range(n - m + 1) :
        for j in range(m) : # 문자열의 각 요소마다 찾아야할 문자열 확인
            if my_str[i+j] != to_find[j] :
                break
        else :
            cnt += 1
    
    print('#{} {}'.format(test_case, cnt))