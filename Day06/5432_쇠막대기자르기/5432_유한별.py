# 5432_쇠막대기 자르기
# 2022-08-12

#import sys
#sys.stdin = open('input.txt','r')

def my_len(my_str) :
    cnt = 0
    for _ in my_str :
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1) :
    bars = input()
    n = my_len(bars)
    level = 0
    pieces = 0
    idx = 0
    
		# level은 현재 쇠막대기의 개수, pieces는 총합, idx는 현재 위치
    while idx < n :
        if bars[idx] == '(' :
						# 레이저일 때(지금까지의 쇠막대기 개수만큼 총합 +)
            if bars[idx+1] == ')' :
                pieces += level
                idx += 2
						# 아닐 경우(쇠막대기 개수 + 1)
            else :
                level += 1
                idx += 1
				# 쇠막대기가 끝났을 때 쇠막대기 개수 -1, 총합 + 1 
        else :
            pieces += 1
            level -= 1
            idx += 1
    
    print('#{} {}'.format(tc,pieces))