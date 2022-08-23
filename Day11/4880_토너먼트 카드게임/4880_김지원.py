# 4880_토너먼트 카드게임
# 220823
'''
설계 13:06 ~ 13:09
구현 13:19 ~ 14:58
'''



import sys
sys.stdin = open('input.txt','rt')

# 가위바위보 승리 경우 결과 저장
result = {
    1 : 3,
    2 : 1,
    3 : 2,
}

T = int(input())

# 가위바위보 게임 결과를 반환하는 함수
def game(i, j):
    # 비긴 경우 작은 것 반환
    if student[i] == student[j]:
        return i
    else:
        # i번호가 이긴 경우
        if result.get(student[i]) == student[j]:
            return i
        # j번호가 이긴 경우
        else:
            return j
    
    

# 그룹을 절반으로 나누는 함수 i ~ j
def group(i, j):
    # 그룹내에 혼자인 경우
    if i == j:
        return i
    # 그룹내에 2명만 남은 경우
    if i + 1 == j:
        return game(i, j)
    # 그외
    else:
        return game(group(i, (i+j)//2), group((i+j)//2 + 1, j))



for tc in range(1, T+1):
    N = int(input())
    student = list(map(int, input().split()))

    answer = group(0, N-1)

    print('#{} {}'.format(tc, answer+1))