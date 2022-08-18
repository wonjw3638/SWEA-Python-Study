import sys
sys.stdin = open('input.txt','r')
bun = int(input())

# list 길이 계산
def ll(a):
    cnt = 0
    for i in a:
        cnt+=1
    return cnt

for he in range(1,bun+1) :
    n = input()
    lst = []
    for i in n :
        
        # 중복된값 빼주기
        if lst and i == lst[-1] :
            lst.pop()
        
        # 빈 리스트에 중복되지 않은 값만 넣어주기
        else :
            lst.append(i)

    print('#{} {}'.format(he, ll(lst)))

