import sys
sys.stdin = open('input.txt', 'r')

# 중위순회를 이용하여 자식 세주기
def inorder(n):
    global cnt
    if n:
        inorder(ch1[n])
        cnt+=1
        inorder(ch2[n])
    return cnt

bun = int(input())
for hs in range(1, bun+1):
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt=0
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    # 자식을 인덱스로 부모 번호 저장
    for i in range(E):
        p,c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    print('#{} {}'.format(hs, inorder(N)))