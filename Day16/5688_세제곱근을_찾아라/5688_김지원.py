# 5688_세제곱근을 찾아라
# 220916

'''
09:13~
'''
import sys
sys.stdin = open('input.txt','rt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    start = 1
    end = N
    while True:
        mid = (start+end)//2
        num = (mid**3)
        # 값을 찾은 경우
        if num == N:
            answer = mid
            break
        else:
            # 찾은 값의 결과가 더 크면 중간값을 끝으로
            if num > N:
                # 이미 최적의 값인데 값이 안나옴
                if (end == mid):
                    answer = -1
                    break
                else:
                    end = mid
            # 찾은 값의 결과가 더 작으면 중간값을 처음으로
            else:
                # 이미 최적의 값인데 값이 안나옴
                if (start == mid):
                    answer = -1
                    break
                else:
                    start = mid

    print('#{} {}'.format(tc, answer))