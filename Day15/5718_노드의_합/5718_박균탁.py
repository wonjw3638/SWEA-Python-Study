import sys
sys.stdin = open('input.txt', 'r')

bun = int(input())

for hs in range(1,bun+1):
    a, b, c = map(int,input().split())
    tree = [0 for _ in range(a+1)]
    for _ in range(b):
        idx, value = map(int, input().split())
        tree[idx] = value       # 노드의 값을 저장

    for i in range(a, 0, -1):
        if i // 2 > 0:
            tree[i // 2] += tree[i]        # 자식 노드는 부모 노드의 *2, *2 +1 이므로 뒤에서부터 2개씩 연산

    print("#{} {}".format(hs, tree[c]))

