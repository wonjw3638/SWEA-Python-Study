# 1216_회문2
# 2022-08-16

#import sys
#sys.stdin = open('input.txt','r')

# len 대체 함수
def my_len(arr) :
    cnt = 0
    for a in arr :
        cnt += 1
    return cnt


# max 대체 함수
def my_max(a, b) :
    if a >= b :
        return a
    else :
        return b


# 1차원 list가 주어졌을 때 최대 회문 길이 구하기
def palindrome(arr) :
    max_cnt = 0
    for n in range(1, 101) :
        for idx in range(0, 101-n) :
            new_str = arr[idx:idx+n]
            if new_str == new_str[::-1] :
                max_cnt = my_max(n, max_cnt)
    return max_cnt


# main 문
for test_case in range(1, 11) :
    tc = input()
    table = []
    for i in range(100) :
        table.append(list(input()))

    max_cnt = 0
    for i in range(100) :
        # row 검사
        max_cnt = my_max(max_cnt, palindrome(table[i]))
        
        # col 검사
        check_arr = []
        for j in range(100) :
            check_arr.append(table[j][i])
        max_cnt = my_max(max_cnt, palindrome(check_arr))
    
    print('#{} {}'.format(test_case, max_cnt))