# 4839_이진탐색
# 2022-08-11 

# import sys
# sys.stdin = open('input.txt','r')

T = int(input())

def find_page(s_idx, e_idx, dest) : # 재.귀.조.아
    m_idx = int((s_idx + e_idx)/2) # 중간 페이지값 찾기

    if m_idx == dest : # 값이 맞으면 1 리턴
        return 1
    elif m_idx < dest : # 중간페이지 이후에 목표 페이지가 있을 경우
        return find_page(m_idx, e_idx, dest) + 1
    else : # 중간페이지 이전에 목표 페이지가 있을 경우
        return find_page(s_idx, m_idx, dest) + 1

for test_case in range(1, T+1) :
    P, A, B = map(int, input().split())
    cnt_A = find_page(1, P, A)
    cnt_B = find_page(1, P, B)
    print('#{} '.format(test_case), end='')
    if cnt_A < cnt_B :
        print('A')
    elif cnt_A > cnt_B :
        print('B')
    else :
        print(0)