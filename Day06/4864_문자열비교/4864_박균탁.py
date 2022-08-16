import sys
sys.stdin = open('input.txt','r')
bun = int(input())
for he in range(1,bun+1) :
    a = str(input())
    b = str(input())
    # a문자열이 b문자열 안에 존재하면 1 출력하고 아니면 0 출력
    if a in b :
        print('#{} 1'.format(he))
    else :
        print('#{} 0'.format(he))
