# 1219_길찾기
# 2022-08-18

# import sys
# sys.stdin = open('input.txt', 'r')

# 기존 문제들은 모든 노드에 방문이 핵심이었다면
# 이 문제는 모든 루트 방문이 핵심 -> 지나간 루트 중복 check
# 그리고 dfs 때리면 해결
def dfs(node) :
    global flag
    if node == 99 :
        flag = 1
        return
    for i in range(N) :
        if route_check[i] == 0 and route[i][0] == node :
            route_check[i] = 1
            dfs(route[i][1])

for _ in range(10) :
    TC, N = map(int, input().split())
    route_input = list(map(int, input().split()))
    route = []
    route_check = [0 for _ in range(N)]
    flag = 0

    while route_input : 
        end_node = route_input.pop()
        start_node = route_input.pop()
        route.append((start_node, end_node))

    dfs(0)
    print('#{} {}'.format(TC,flag))