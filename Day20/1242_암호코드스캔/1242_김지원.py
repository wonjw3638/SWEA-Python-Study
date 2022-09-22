# 1242 암호코드 스캔
# 220920

'''
설계 10
구현 11:10 ~ 17:37
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 16진수 알파벳 -> 2진수 (어차피 2번 해야하니까 한 번에..)
hex_num = {
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

# 10진수를 4자리 2진수로 변환
def DtoB(dec_num):
    ans = ''
    if dec_num != 0:
        while dec_num>0:
            ans = str(dec_num%2) + ans
            dec_num = dec_num//2
        return '{:04d}'.format(int(ans))
    else:
        return '0000'
        

# 16진수를 2진수 표현으로 변환
def HexToBin(string):
    ans = ''
    for s in string:
        if s in hex_num:
            ans += hex_num.get(s)
        else:
            ans += DtoB(int(s))
    return ans

code = {
    (2, 1, 1) : 0,
    (2, 2, 1) : 1,
    (1, 2, 2) : 2,
    (4, 1, 1) : 3,
    (1, 3, 2) : 4,
    (2, 3, 1) : 5,
    (1, 1, 4) : 6,
    (3, 1, 2) : 7,
    (2, 1, 3) : 8,
    (1, 1, 2) : 9,
}


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(set([input().strip() for _ in range(N)]))
    arr.remove('0'*M)
    
    visited = list()
    ans = 0
    for i in range(len(arr)):
        arr_binary = HexToBin(arr[i])
        arr_binary = arr_binary.rstrip('0')

        num_list = list()
        n1 = n2 = n3 = n4 =0
        for j in range(len(arr_binary)-1,-1,-1):
            if arr_binary[j] =='1' and n3 ==0:
                n4+=1
            elif arr_binary[j] == '0' and n2==0:
                n3+=1
            elif arr_binary[j] == '1' and n1==0:
                n2+=1
            elif arr_binary[j]=='0':
                if arr_binary[j-1]=='1':
                    n = min(n2,n3,n4)
                    num_list.append(code.get((n2//n, n3//n, n4//n)))
                    n2 = n3 = n4 = 0
                    if len(num_list) == 8:
                        if ((num_list[7]+num_list[5]+num_list[3]+num_list[1])*3 +(num_list[6]+num_list[4]+num_list[2])+num_list[0])%10 == 0 and num_list not in visited:
                            ans += sum(num_list)
                            visited.append(num_list)
                        num_list = list()
 
    print(f'#{tc} {ans}')