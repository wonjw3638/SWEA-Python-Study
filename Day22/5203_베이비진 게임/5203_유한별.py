from collections import defaultdict

def is_babygin(player):
    for value in player.values():
        if value == 3:
            return True
    for i in range(8):
        if player[i] > 0 and player[i+1] > 0 and player[i+2] > 0:
            return True
    return False

T = int(input())

for tc in range(1, T+1):
    input_arr = list(map(int, input().split()))
    player_1 = defaultdict(int)
    player_2 = defaultdict(int)
    answer = 0

    for idx, item in enumerate(input_arr):
        if idx%2:
            player_2[item] += 1
            if is_babygin(player_2):
                answer = 2
                break
        else:
            player_1[item] += 1
            if is_babygin(player_1):
                answer = 1
                break

    print('#{} {}'.format(tc, answer))