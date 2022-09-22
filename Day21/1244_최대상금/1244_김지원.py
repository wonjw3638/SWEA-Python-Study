# 1244 최대상금
# 220921

'''
2시간40분.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def change(changeArr, i, n):
    global answer

    # 횟수를 모두 소모하면 값 비교 후에 큰 값 저장
    if n == 0:
        tmp = ''.join(map(str, changeArr))
        answer = max(answer, tmp)
        return

    # index값이 마지막까지 탐색했다면 어차피 맨 뒤에 두개만 바꿀 거니까 하나 뺴줌
    if i >= N-1:
        i -= 1
        
    # 이미 정렬된 상태
    if changeArr == numSort:
        # 남은 횟수가 홀수일 때
        if n % 2:
            # 가장 큰 값이 2개 이상이라면 걔네끼리 바꾸면 됨
            if changeArr.count(changeArr[0]) > 1:
                answer = ''.join(map(str, changeArr))
                return
            # 그게 아니라면 맨 뒤에 두개끼리 자리 바꿔줌
            else:
                changeArr[-1], changeArr[-2] = changeArr[-2], changeArr[-1]
                change(changeArr, i+1, 0)
        # 남은 횟수가 짝수면 도달 할 수 있으므로 리턴
        else:
            answer = ''.join(map(str, changeArr))
            return
    else:
        # i index부터 뒤에 있는 값들 비교
        for idx in range(i, N-1):
            for jdx in range(idx+1, N):
                    # 뒤에 위치한 값이 더 큰 경우엔 자리 바꿔줌
                    if changeArr[idx] <= changeArr[jdx]:
                        changeArr[idx], changeArr[jdx] = changeArr[jdx], changeArr[idx]
                        change(changeArr, idx+1, n-1)
                        changeArr[idx], changeArr[jdx] = changeArr[jdx], changeArr[idx]
                    # 뒤에 있는 값이 더 크면 맨뒤에 두개만 바꿔줌
                    else:
                        changeArr[-1], changeArr[-2] = changeArr[-2], changeArr[-1]
                        change(changeArr, idx+1, 0)
                        changeArr[-1], changeArr[-2] = changeArr[-2], changeArr[-1]



for tc in range(1, T+1):
    numbers, M = list(input().split())
    M = int(M)
    # 정렬을 위해서 리스트화 시켜줌
    N = len(numbers)
    
    numbers = list(numbers)
    numSort = numbers[:]
    # 최적의 값
    numSort.sort(reverse=True)

    answer = '0' * N
    change(numbers, 0, M)

    print('#{} {}'.format(tc, answer))