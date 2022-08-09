T = int(input())

for test_case in range(1, T+1) :
    N = int(input())
    cards = list(map(int,input()))
    cnt_card = [0 for _ in range(10)] # 카드 갯수를 counting 할 list 생성
    for card in cards : # 해당 카드 번호를 idx로 갖는 list에 counting
        cnt_card[card] += 1
        
    max_card = 0
    max_cnt = 0
    for idx, card in enumerate(cnt_card) : # max_cnt 찾기
        if max_cnt <= card :
            max_cnt = card
            max_card = idx
    
    print('#{} {} {}'.format(test_case, max_card, max_cnt))