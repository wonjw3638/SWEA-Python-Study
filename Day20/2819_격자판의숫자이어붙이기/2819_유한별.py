# 2819_격자판의 숫자 이어붙이기
# 2022-09-20

def dfs(now_i, now_j):
    global redup
    global num
    global cnt


    if cnt == 7:
        redup.add(''.join(num))
        return
    for k in range(4):
        new_i = now_i+d_i[k]
        new_j = now_j+d_j[k]
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            num[cnt]= table[now_i][now_j]
            cnt += 1
            dfs(new_i, new_j)
            cnt -= 1
            num[cnt] = 0



T = int(input())
d_i = [0, 0, 1, -1]
d_j = [1, -1, 0, 0]

for tc in range(1, T+1):
    table = []
    redup = set()
    num = [0 for _ in range(7)]

    for _ in range(4):
        table.append(list(input().split()))
    
    for i in range(4):
        for j in range(4):
            cnt = 0
            dfs(i, j)
    
    print('#{} {}'.format(tc, len(redup)))