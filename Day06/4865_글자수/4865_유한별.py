# 4865_글자수
# 2022-08-16

#import sys
#sys.stdin = open('input.txt','r')

T = int(input())
alpha = {}

for test_case in range(1, T+1) :
    # 'A'-'Z'를 key로 하는 dict 생성(초기 value = 0)
    for i in range(26) :
        alpha[chr(65+i)] = 0

    str1 = list(input())
    str2 = list(input())

    # str2의 알파뱃 개수를 count하여 dict에 반영
    for char in str2 :
        alpha[char] += 1

    # str1의 각 글자마다 dict에서 개수를 확인하여 max값 찾기
    max_char = 0
    for char in str1 :
        if alpha[char] > max_char :
            max_char = alpha[char]

    print('#{} {}'.format(test_case, max_char))