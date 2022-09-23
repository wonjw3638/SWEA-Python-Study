from collections import defaultdict

T = int(input())
direction = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    microbe = []

    for _ in range(K):
        microbe.append(list(map(int, input().split())))

    while M > 0:
        to_del = []
        hash_table = defaultdict(list)

        for m in microbe:
            # 각 미생물 이동
            m[0]+=direction[m[3]][0]
            m[1]+=direction[m[3]][1]
            if m[0] == 0 or m[0] == N-1 or m[1] == 0 or m[1] == N-1:
                m[2] //=2
                if m[3]%2:
                    m[3]+=1
                else:
                    m[3]-=1
            hash_table[(m[0], m[1])].append((m[2], m[3]))

        # 해시테이블을 활용 해같은 칸에 미생물들이 들어왔을 때 처리
        to_del_key = []
        for key in hash_table.keys():
            if len(hash_table.get(key)) <= 1: continue
            max_m = float('-INF')
            max_dir = -1
            sum_m = 0
            for m in hash_table.get(key):
                sum_m += m[0]
                if max_m < m[0]:
                    max_m = m[0]
                    max_dir = m[1]
            hash_table[key] = [(sum_m, max_dir)]

        microbe = []
        for key, value in hash_table.items():
            microbe.append((list(key)+list(hash_table.get(key)[0])))

        M -= 1

    answer = 0
    for m in microbe:
        answer += m[2]
    print('#{} {}'.format(tc, answer))