# 1240 단순 2진 암호코드
# 220919

import sys
sys.stdin = open('input.txt','rt')

T = int(input())

# 코드 변환하는 dictionary
code = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [ input() for _ in range(N) ]

    for i in range(N):
        tmp = arr[i][::-1]
        # 한 행에 1이 들어있다면 가장 마지막 1의 인덱스 값을 찾음
        if '1' in tmp:
            index1 = M - (tmp.index('1'))
            tmp = tmp[::-1]
            break
        else:
            continue
    
    # 가장 마지막 1로부터 56개의 숫자들로 암호문 찾기
    arr_code = tmp[index1-56:index1+1]

    odd = even = 0
    # 암호문을 7개씩 나누면서 홀수번째, 짝수번째 수 합하기
    for idx in range(8):
        num = code.get(arr_code[idx*7:(idx+1)*7])
        if idx%2:
            even += num
        else:
            odd += num
    
    total = (odd * 3) + even

    if total%10:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, odd+even))