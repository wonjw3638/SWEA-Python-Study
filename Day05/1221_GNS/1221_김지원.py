# 1221 - GNS
# 220812

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for _ in range(1, T + 1):
    tc, N = list(input().split())
    print(tc)
    str_list = list(input().split())
    str_count = [0] * 10  # 숫자가 등장하는 횟수 세기
    string = {            # 문자열 - 숫자 대응하는 dictionary 생성
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9,
    }

    for s in str_list:     # 등장하는 횟수 세기
        str_count[string.get(s)] += 1

    idx = 0
    for key in string.keys():    # 키값을 통해 인덱스 접근, 횟수만큼 출력
        for _ in range(str_count[idx]):
            print(key, end=' ')
        idx += 1
    print()