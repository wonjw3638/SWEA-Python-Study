import sys
sys.stdin = open('input.txt','r')
W = int(input())
for he in range(1, W+1) :
    n, m = map(int, input().split()) # 숫자 n개를 m개씩 묶어서 계산
    num = list(map(int, input().split())) # 숫자 입력값
    top = 0
    bottom = 0
    for a in num :
        bottom += a # 모든 항목을 더해서 최대값 만들기
    for i in range(n-(m-1)): # i개 뽑아서 합치기  

        result = 0 # 테스트 케이스마다 result값을 0으로 변환
        for j in range(m) :
            result += num[j+i]
            
    
        if top <= result :
            top = result # 최대값 찾기
        if result <= bottom :
            bottom = result # 최소값 찾기
    print(f'#{he} {top - bottom}')
    