import sys
sys.stdin = open('input.txt','r')
bun = int(input())


for he in range(1,bun+1) :
    cnt = 0
    n, k = map(int, input().split())
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    for i in range(1<<12) : # 원소가 12개일 경우의 모든 부분집합
        cnt2 = 0  
        tot = 0   
        for j in range(12) :
            if i & (1<<j) : 
                cnt2 += 1 # 부분집합의 개수
                tot += arr[j] # 부분집합의 합
        if tot == k and cnt2 == n:
            cnt += 1
        

    print('#{} {}'.format(he, cnt))