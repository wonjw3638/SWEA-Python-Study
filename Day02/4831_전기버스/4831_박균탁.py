import sys
sys.stdin = open('input.txt','r')
W = int(input())
for he in range(1, W+1) :
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    pos = 0 # 현재 위치
    cnt = 0 # 충전 횟수

    while pos + k < n : # 거리가 n 안일경우
        for i in range(k,0,-1) :
            if pos + i in charge : # 이동거리 안에 충전소 있는지 파악
                cnt += 1 # 충전 횟수 최신화
                pos += i # 위치 최신화      
                break
        else :  
            cnt = 0 # 이동거리 안에 충전소 없으면 0 리턴
            break

    print(f'#{he} {cnt}')





        