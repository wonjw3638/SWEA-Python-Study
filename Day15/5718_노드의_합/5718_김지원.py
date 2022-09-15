# 5718_노드의 합
# 220915

'''
10:06 ~ 10:14
'''
import sys
sys.stdin = open('input.txt','rt')

def postorder_traverser(node):
    # 저장된 값이 없는 node인 경우
    if not tree[node]:
        x = y = 0
        if 2 * node <= N:
            x = postorder_traverser(2 * node)
        if (2 * node) + 1 <= N:
            y = postorder_traverser((2 * node) + 1)
        return x + y
    # 저장된 값이 있는 node인 경우
    else:
        return tree[node]

T = int(input())

for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))

    tree = [0] * (N+1)

    # 트리 정보 저장
    for _ in range(M):
        idx, num = list(map(int, input().split()))
        tree[idx] = num

    answer = postorder_traverser(L)

    print('#{} {}'.format(tc, answer))