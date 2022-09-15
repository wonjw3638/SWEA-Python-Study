# 5714_subtree
# 220915

'''
09:50~10:00
'''
import sys
sys.stdin = open('input.txt','rt')


# 전위 순회 방식 사용
def preorder_traverse(node):
    global answer
    answer += 1
    if ch1[node]:
        preorder_traverse(ch1[node])
    if ch2[node]:
        preorder_traverse(ch2[node])


T = int(input())

for tc in range(1, T+1):
    E, N = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    # 트리 정보 저장
    for e in range(0, 2 * E, 2):
        # 왼쪽 자식 노드 값이 비어있으면
        if not ch1[arr[e]] :
            ch1[arr[e]] = arr[e+1]
        else:
            ch2[arr[e]] = arr[e+1]
    
    # subtree의 노드 개수세기
    answer = 0
    preorder_traverse(N)
    
    print('#{} {}'.format(tc, answer))