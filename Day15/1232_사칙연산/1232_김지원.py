# 1232_사칙연산
# 220915
'''
09:15 ~09:46
'''

import sys
sys.stdin = open('input.txt','rt')


operation = {
    '+' : lambda x, y : x + y,
    '-' : lambda x, y : x - y,
    '*' : lambda x, y : x * y,
    '/' : lambda x, y : x // y,
}


def inorder_traverse(node):
    # 정수인 경우 (마지막 노드)
    if type(tree[node]) != list:
        return tree[node]
    
    # 왼쪽 노드 탐색
    x = inorder_traverse(tree[node][1])
    # 현재 노드 탐색 (연산자)
    oper = tree[node][0]
    # 오른쪽 노드 탐색
    y = inorder_traverse(tree[node][2])

    return operation[oper](x, y)

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)

    for _ in range(N):
        num = list(input().split())
        # 입력 값이 연산자인 경우
        if len(num) > 2:
            tree[int(num[0])] = [num[1]] + list(map(int, num[2:]))
        # 입력 값이 정수인 경우
        else:
            tree[int(num[0])] = int(num[1])

    answer = inorder_traverse(1)

    print('#{} {}'.format(tc, answer))