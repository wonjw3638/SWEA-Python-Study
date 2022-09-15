# 4861_회문
# 220816
# 설계 9:15 ~ 9:18 - 3
# 구현 9:20 ~ 9:32 - 12

import sys
sys.stdin = open('input.txt','r')

T = int(input())

# 회문 찾는 함수 만들기
def palindrome(string, N, M):
    # 행에서 찾기
    for s in string:
        for k in range(N - M + 1):
            answer = s[0+k:M+k]
            if answer == answer[::-1]:
                return answer
    
    # 열에서 찾기
    for j in range(N):
        for k in range(N - M + 1):
            for i in range(M):
                answer += string[i + k][j]
            if answer == answer[::-1]:
                return answer
            answer = ''

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    string = [input() for _ in range(N)]
    answer = palindrome(string, N, M)

    print('#{} {}'.format(tc, answer))