def heap(now):
    global tree
    if now >= 2:
        if tree[now] < tree[now//2]:
            tree[now], tree[now//2] = tree[now//2], tree[now]
            heap(now//2)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = list(map(int, input().split()))
    node = len(tree)
    tree.insert(0, 0)
    for i in range(1, node+1):
        heap(i)
    
    answer = 0
    while node > 0:
        node //= 2
        answer += tree[node]
    
    print('#{} {}'.format(tc, answer))
    print(tree)