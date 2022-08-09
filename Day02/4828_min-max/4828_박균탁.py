import sys
sys.stdin = open('input.txt','r')
W = int(input())
for he in range(1, W+1) :
    n = int(input())
    card = list(map(int, input().split())) 
    print(card)
    max = 0
    min = 1000000
    for i in card :
        if max <= i :
            max = i
        elif i <= min :
            min = i
    print(max, min)
    print(f'#{he} {max - min}')
