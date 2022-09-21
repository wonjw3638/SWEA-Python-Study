T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    bin_M = bin(M)[2:]
    bin_M = '0' * (28-len(bin_M)) + bin_M
    flag = True
    for i in range(1, N+1):
        if bin_M[28-i] == '0':
            flag = False
            break

    if flag: print('#{} {}'.format(tc, 'ON'))
    else: print('#{} {}'.format(tc, 'OFF'))