# 4861_회문
# 2022-08-16

#import sys
#sys.stdin = open('input.txt','r')

# 내장함수 len 대체
def my_len(arr) :
    cnt = 0
    for a in arr :
        cnt += 1
    return cnt


# 회문 검사하는 함수
def palindrome(arr) :
    for i in range(N-M+1) :
        idx = 0
        pal = []
        # 새로운 list를 만들거라 M까지 다 돌림
        while idx < M :
            pal.append(arr[i+idx])
            if pal[idx] != arr[i+M-1-idx] :
                break
            idx += 1

        # 만약 새로운 list가 온전한 회문이면 M의 크기로 만들어짐
        if my_len(pal) == M :
            for j in range(M) :
                print(pal[j], end='')
            print()
            return 1
    return 0


T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    table = []
    flag = 0

    for i in range(N) :
        table.append(list(input()))

    print('#{}'.format(test_case), end=' ')
    for i in range(N) :
        # row 검사
        if palindrome(table[i]) :
            break
        
        # col 검사
        check_arr = []
        for j in range(N) :
            check_arr.append(table[j][i])
        if palindrome(check_arr) :
            break