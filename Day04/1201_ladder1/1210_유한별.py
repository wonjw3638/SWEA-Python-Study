# 1210_Ladder1
# 2022-08-11 

#import sys
#sys.stdin = open('input.txt')

for _ in range(10) :
    test_case = int(input())
    ladders = [0 for _ in range(100)]
    idx = 0
    for i in range(100) :
        ladders[i] = list(map(int, input().split()))
        if i == 99 :
            for j in range(100) :
                if ladders[i][j] == 2 :
                    idx = j
            
    floor = 99
    while floor > 0 : # 위쪽으로 올라가면서 탐색
        if 0 < idx < 99 : # 가장자리 제외
            if ladders[floor][idx + 1] == 1 : # 오른쪽 길을 만났을 때
                ladders[floor][idx] = 0
                idx += 1
                continue
            elif ladders[floor][idx - 1] == 1: # 왼쪽 길을 만났을 때
                ladders[floor][idx] = 0
                idx -= 1
                continue
            else : # 아닐 경우 수직상승
                floor -= 1
        elif idx == 0 : # 왼쪽 가장자리일때(idx 에러를 방지하기 위함)
            if ladders[floor][idx + 1] == 1 : # 오른쪽 길만 체크
                ladders[floor][idx] = 0
                idx += 1
                continue
            else :
                floor -= 1
            
        else : # 오른쪽 가장자리
            if ladders[floor][idx - 1] == 1: # 왼쪽 길만 체크
                ladders[floor][idx] = 0
                idx -= 1
                continue
            else :
                floor -= 1
    
    print('#{} {}'.format(test_case, idx))