def synergy(put_list):
    result = 0
    for i in range(N):
        if put_list[i]:
            for j in range(i+1, N):
                if put_list[j]:
                    result += table[i][j] + table[j][i]
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    table = []
    for _ in range(N):
        table.append(list(map(int, input().split())))

    A_list = [0 for _ in range(N)]
    B_list = [0 for _ in range(N)]
    answer = 1<<31

    for i in range(1<<N):
        B_list = [0 for _ in range(N)]
        for j in range(N):
            if i & (1<<j):
                B_list[j] = 1
        if sum(B_list) != N//2:
            continue

        for j in range(N):
            A_list[j] = B_list[j]^1
        
        tmp_A = synergy(A_list)
        tmp_B = synergy(B_list)
        answer = min(abs(tmp_A-tmp_B), answer)
    
    print('#{} {}'.format(tc, answer))