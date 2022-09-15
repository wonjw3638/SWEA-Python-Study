import sys
sys.stdin = open('input.txt','r')
bun = int(input())
# 길이를 구하기 위해 llengthh 함수 생성
def llengthh(a) :
    cnt = 0
    for _ in a:
        cnt += 1
    return cnt
for he in range(1,bun+1) :
    A, B = list(map(str, input().split()))
    A_l = list(A)
    B_l = list(B)
    lst = []
    ant = 0
    bnt = 0
    # B가 A안에 얼마나 있는지 확인하기 위해서 B의 길이만큼 A 나누기                                 
    for i in range(llengthh(A)+1-llengthh(B)) :
        lst.append(A_l[i:i+llengthh(B)])
    # B_l 이 A_l 안에 얼마나 있는지 계산
    for i in range(llengthh(lst)):
        if B_l == lst[i] :
            bnt += 1    
    # A의 총 길이 구하기
    for i in A :
        ant += 1
    # A의 길이에서 B의 길이를 빼기
    # 여기서 B의 길이만큼 입력횟수가 줄지만 B도 결국 입력1이 들어가기에 1 빼주기
    ans = ant - ((llengthh(B_l)-1) * bnt)
    print('#{} {}'.format(he, ans))
    
    