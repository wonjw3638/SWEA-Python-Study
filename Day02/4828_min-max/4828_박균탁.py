import sys
sys.stdin = open('input.txt','r')
W = int(input())
for he in range(1, W+1) :
    n = int(input()) # 숫자 개수 반환
    card = list(map(int, input().split())) # 숫자 쪼개기
    print(card)
    max = 0 # 숫자 값이 0부터 시작이므로
    min = 1000000 # 숫자 값이 1000000까지 이므로
    for i in card :
        if max <= i :
            max = i # 최대값 찾기
        elif i <= min :
            min = i # 최소값 찾기
    print(f'#{he} {max - min}')
