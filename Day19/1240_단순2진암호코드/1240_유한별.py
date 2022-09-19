import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
# 암호 매칭 dict
code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = []

    for _ in range(N):
        table.append(input())

    line = -1
    right_idx = -1
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            # 오른쪽 끝 값은 무조건 1 이므로 오른쪽 끝 값을 기준으로 체크
            if table[i][j] == '1':
                line = i
                right_idx = j
                break
        if right_idx != -1:
            break
    # 내가 볼 줄 한줄만 확인
    left_idx = right_idx - 55
    cnt = 0
    odd_nums, even_nums = 0, 0
    for i in range(left_idx, right_idx+1, 7):
        # 홀수 자리 처리
        if cnt%2:
            odd_nums += code.get(table[line][i:i+7])
        # 짝수 자리 처리
        else:
            even_nums += code.get(table[line][i:i+7])
        cnt+=1

    # 10으로 나누어 떨어지는지 확인
    result = 0 if (odd_nums+even_nums*3)%10 else (odd_nums)+(even_nums)
    print('#{} {}'.format(tc, result))