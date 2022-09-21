def is_valid(point):
    i = point[0]
    j = point[1]
    if 0 <= i < N and 0 <= j < N: 
        return True
    else: 
        return False


def search(now_i, now_j):
    global max_len

    for side_1 in range(1, N):
        for side_2 in range(1, N):
            p0 = (now_i, now_j)
            p1 = (p0[0]+d_i[0]*side_1, p0[1]+d_j[0]*side_1)
            p2 = (p1[0]+d_i[1]*side_2, p1[1]+d_j[1]*side_2)
            p3 = (p2[0]+d_i[2]*side_1, p2[1]+d_j[2]*side_1)
            flag = True
            if is_valid(p1) and is_valid(p2) and is_valid(p3):
                redup = list()
                for k in range(side_1):
                    if table[p0[0]+d_i[0]*k][p0[1]+d_j[0]*k] in redup:
                        flag = False
                        break
                    else:
                        redup.append(table[p0[0]+d_i[0]*k][p0[1]+d_j[0]*k])
                for k in range(side_2):
                    if table[p1[0]+d_i[1]*k][p1[1]+d_j[1]*k] in redup:
                        flag = False
                        break
                    else:
                        redup.append(table[p1[0]+d_i[1]*k][p1[1]+d_j[1]*k])
                for k in range(side_1):
                    if table[p2[0]+d_i[2]*k][p2[1]+d_j[2]*k] in redup:
                        flag = False
                        break
                    else:
                        redup.append(table[p2[0]+d_i[2]*k][p2[1]+d_j[2]*k])
                for k in range(side_2):
                    if table[p3[0]+d_i[3]*k][p3[1]+d_j[3]*k] in redup:
                        flag = False
                        break
                    else:
                        redup.append(table[p3[0]+d_i[3]*k][p3[1]+d_j[3]*k])
                if flag:
                    max_len = max(max_len, len(redup))
    

T = int(input())

d_i = [1, 1, -1, -1]
d_j = [1, -1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    table = []
    for _ in range(N):
        table.append(list(map(int, input().split())))
    visited = [[False for _ in range(N)] for _ in range(N)]
    desserts = []
    max_len = -1

    for i in range(N):
        for j in range(N):
            search(i, j)
    
    print('#{} {}'.format(tc, max_len))