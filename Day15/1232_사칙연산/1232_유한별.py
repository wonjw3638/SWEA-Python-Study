# 노드 클래스 구현(연결리스트 활용)
class Node:
    def __init__(self, value=None, l_value=None, r_value=None):
        self.value = value
        self.l_value = l_value
        self.r_value = r_value


# 중위 순회 구현
def inorder(node):
    # Full Binary Tree이기 때문에 자식 노드가 0개 or 2개
    if nodes[node].l_value is None:
        return nodes[node].value
    # 자식노드가 2개일 경우 무조건 연산자 -> 연산 처리
    else:
        return operate(inorder(nodes[node].l_value), inorder(nodes[node].r_value), nodes[node].value)


# 연산 처리 함수
def operate(num1, num2, op):
    ops = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x/y,
    }
    return ops[op](num1, num2)


T = 10
operator = ['+', '-', '*', '/',]

for tc in range(1, T+1):
    N = int(input())
    input_arr = []

    nodes = [Node() for _ in range(1001)]
    for i in range(N):
        input_arr.append(list(input().split()))
        node_num = int(input_arr[i][0])

        # 노드의 값이 연산자일 경우(자식 노드 생성)
        if input_arr[i][1] in operator:
            nodes[node_num].value = input_arr[i][1]
            nodes[node_num].l_value = int(input_arr[i][2])
            nodes[node_num].r_value = int(input_arr[i][3])
        # 노드의 값이 숫자일 경우(자식 노드 생성 X)
        else:
            nodes[node_num].value = int(input_arr[i][1])
    
    print('#{} {}'.format(tc, int(inorder(1))))