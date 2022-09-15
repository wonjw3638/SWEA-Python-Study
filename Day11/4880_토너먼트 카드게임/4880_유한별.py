# 4880_토너먼트 카드게임
# 2022-08-23

# 승리 index를 찾는 함수
def check(left, right):
    global N
    global cards

    # 만약 범위 내의 값이 2개 일 때
    if left+1 == right:
        # 가위바위보 실행
        # 이긴 index return
        if play(cards[left], cards[right]):
            return left
        else:
            return right
    # 만약 범위 내의 값이 1개 일 때
    # index return
    elif left == right:
        return left
    # 범위가 3 이상일 때
    else:
        # 왼쪽, 오른쪽으로 나눠서 재귀호출
        # 각 부분에서 얻은 index 저장
        left_idx = check(left, (left+right)//2)
        right_idx = check((left+right)//2+1, right)
        # 양쪽 index의 값으로 가위바위보 실행
        # 승리한 indeex return
        if play(cards[left_idx], cards[right_idx]):
            return left_idx
        else:
            return right_idx


# 가위바위보 : 좌측이 이기면 True, 우측이 이기면 False return
def play(a, b):
    if a == b:
        return True
    elif a == b+1 or a == b-2:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    idx = -1
    print('#{} {}'.format(tc, check(0, N-1) + 1))