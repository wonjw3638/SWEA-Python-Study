T = int(input())
direction = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    microbe = []
    for _ in range(K):
        microbe.append(list(map(int, input().split())))

    while M > 0:
        to_del = []
        for m in microbe:
            m[0]+=direction[m[3]][0]
            m[1]+=direction[m[3]][1]
            if m[0] == 0 or m[0] == N-1 or m[1] == 0 or m[1] == N-1:
                m[2] //=2
                if m[3]%2:
                    m[3]+=1
                else:
                    m[3]-=1
        
        for i in range(K):
            for j in range(i+1, K):
                if microbe[i][0] == microbe[j][0] and microbe[i][1] == microbe[j][1]:
                    if microbe[i][2] > microbe[j][2]:
        M -= 1

    answer = 0
    for m in microbe:
        answer += m[2]
    print('#{} {}'.format(tc, answer))
    
    # 이따가 마저 풀거임