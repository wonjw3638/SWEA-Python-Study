# 5249 최소 신장 트리
# 220929

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def find(x):
    if x != Ptree[x]:
        return find(Ptree[x])
    else: return x

def union(x, y):
    Ptree[find(y)] = find(x)


for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(E)]
    
    # 가중치를 기준으로 정렬
    arr.sort(key=lambda x : x[2])
    Ptree = [i for i in range(V+1)]

    answer = 0

    # 간선들의 값 불러오기
    for n1, n2, w in arr:
        if find(n1) != find(n2):
            answer += w
            union(n1, n2)

    print('#{} {}'.format(tc, answer))