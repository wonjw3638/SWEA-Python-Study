import sys
sys.stdin = open('input.txt','r')
bun = int(input())
def binarySearch(r, key) :
    l = 1
    end = r
    cnt = 0
    while l <= end :
        c = (l+r)//2 # 중간값 찾기
        cnt += 1 # 횟수 반환
        if c == key :
            return cnt
        elif c > key : # 중간값이 결과보다 크면
            r = c # 검색범위중 끝부분 줄이기
        else : # 중간값이 결과보다 작으면
            l = c # 검색범위중 시작부분 늘리기
for he in range(1,bun+1) :
    
    r, result1, result2 = map(int, input().split()) # 입력값 받기
    cnt1 = binarySearch(r, result1) # A에 대한 검색횟수
    cnt2 = binarySearch(r, result2) # B에 대한 검색횟수

    if cnt1 < cnt2 :
        print('A')
    elif cnt1 > cnt2 :
        print('B')
    else :
        print('O')

