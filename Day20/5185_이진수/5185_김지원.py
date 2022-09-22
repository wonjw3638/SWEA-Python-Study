# 5185 이진수
# 220919

'''
09:22~38
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 16진수
conv_hex = {
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15,
}

# 10진수를 2진수로 변환
def DtoB(dec_num):
    ans = ''
    if dec_num == 0:
        return '0000'
    else:
        while dec_num > 0:
            ans = str(dec_num%2) + ans
            dec_num = dec_num//2
        return "{:04d}".format(int(ans))
        

for tc in range(1, T+1):
    N, hex_num = list(input().split())
    answer = ''
    for h in hex_num:
        if h in conv_hex:
            h = conv_hex.get(h)
        else:
            h = int(h)

        answer += DtoB(h)
    
    print('#{} {}'.format(tc, answer))