# 5177_이진 힙
# 220915

'''
10:35~11:25
'''
import sys
sys.stdin = open('input.txt','rt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    arr = list(map(int, input().split()))

    for idx in range(N):
        tree[1+idx] = arr[idx]
        c = 1+idx
        p = c//2
        while p and tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            c = p
            p = c//2
            
    answer = 0
    # 조상 노드 합 구하기

    node = N//2
    while node:
        answer += tree[node]
        node = node//2

    print('#{} {}'.format(tc, answer))