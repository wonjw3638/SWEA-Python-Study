  
import sys
sys.stdin = open('input.txt','r')
W = int(input())
for he in range(1, W+1) :
    n = int(input()) # 입력된 카드 장수
    card = list(map(int, input())) # 카드 나열
    max_card = 0
    max_cnt = 0
    for i in range(10) : # 0~9까지 찾기
        cnt = 0

        for j in card :
            if j == i : # 해당 숫자가 몇장인지 찾기
                cnt += 1 # cnt의 맥스값 찾기

        if max_cnt <= cnt : 
            max_cnt = cnt   # cnt가 가장 큰 값 찾기
            max_card = i    # 장수가 가장 많은 숫자 중 가장 큰값

    print(f'#{he} 숫자{max_card}, {max_cnt}장')