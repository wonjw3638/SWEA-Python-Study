import sys
sys.stdin = open('input.txt','r')
bun = int(input())

def ll(a):
    cnt = 0
    for i in a:
        cnt+=1
    return cnt

for he in range(1,bun+1) :
    n = int(input())//10
 
    # 등차수열 공식 찾기 An = An-1 + An-2 
    # 초기값 A1, A2설정
    seq = [1,3]

    # n까지 계산해주기
    for i in range(2,n):
        seq.append(seq[i-1] + 2*seq[i-2])
        
    ans = seq[n-1]
    print('#{} {}'.format(he, ans))