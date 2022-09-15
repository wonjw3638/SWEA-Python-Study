import sys
sys.stdin = open('input.txt','r')
bun = int(input())
lan = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"] # 문자열 종류
for he in range(1,bun+1) :
    n = list(map(str,input().split()))
    charge = list(map(str, input().split()))
    ali = []
    for i in range(10) :
        for j in charge:
            if lan[i] == j: # lan 리스트에 정렬할 문자를 순서대로 입력해주고 순서대로 append 해줘서 정렬하기 
                ali.append(j)     
    
    print('#{}'.format(he))
    print(ali)