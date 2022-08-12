# 1221_GNS
# 2022-08-12

#import sys
#sys.stdin = open('input.txt','r')

T = int(input())
# T = int(sys.stdin.readline())
for test_case in range(1, T+1) :
    my_num = {
        'ZRO' : 0,
        'ONE' : 0,
        'TWO' : 0,
        'THR' : 0,
        'FOR' : 0,
        'FIV' : 0,
        'SIX' : 0,
        'SVN' : 0,
        'EGT' : 0,
        'NIN' : 0,
    }

    tc, N = input().split()
#    tc, N = sys.stdin.readline().split()
    N = int(N)
    num_list = input().split()
#    num_list = sys.stdin.readline().split()

    for num in num_list : # map의 key를 찾아 +1씩 해줌
        my_num[num] += 1
    
    print('#{}'.format(test_case),end=' ')
    for k, v in my_num.items() : # dict에 존재하면 출력
        for _ in range(v) :
            print(k, end=' ')
    print()