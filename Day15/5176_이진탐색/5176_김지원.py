# 5716_이진탐색
# 220915

'''
10:21~10:27
'''
import sys
sys.stdin = open('input.txt','rt')


def inorder_traverse(node):
    global num
    # 왼쪽 노드에 값 넣기
    if 2 * node <= N:
        inorder_traverse(2 * node)
    # 노드에 값 넣기
    tree[node] = num
    num += 1
    # 오른쪽 노드에 값 넣기
    if ((2 * node) + 1) <= N:
        inorder_traverse(((2 * node) + 1))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)

    num = 1
    inorder_traverse(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))