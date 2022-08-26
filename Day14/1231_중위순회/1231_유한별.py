# 1231_중위순회 풀이
# 2022-08-26

def my_len(my_str):
    len_cnt = 0
    for _ in my_str:
        len_cnt += 1
    return len_cnt


def dfs(now):
    global visited
    global result

    if now*2 <= N:
        if not visited[now*2]:
            dfs(now*2)
    visited[now] = 1
    result+= nodes[now]
    if (now*2)+1 <= N:
        if not visited[(now*2)+1]:
            dfs((now*2)+1)


for tc in range(1, 11):
    N = int(input())
    nodes = [0 for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    result = ''
    for _ in range(N):
        input_arr = list(input().split())
        nodes[int(input_arr[0])] = input_arr[1]
    bin_len = my_len(bin(N))-2
    start = 1<<(bin_len-1)
    dfs(1)
    print('#{} {}'.format(tc,result))