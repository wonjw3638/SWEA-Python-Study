T = int(input())


for t in range(1, 1+T):
    N = int(input())
    price_list = list(map(int, input().split()))
    all_marg = 0
    for i, a in enumerate(price_list):              # 각 항목별로 파는 가격을 구합니다
        sell_price = a * 1                          # 뒤에 더 높은 가격이 없으면 그대로 팔아서 0이 나오게
        for b in price_list[i+1: N]:                # 파는 가격은 그 항목 뒤에 있는 값중에 가장 큰 값
            if sell_price < b:
                sell_price = b
        margin = sell_price - a                     # 파는 가격 - 원래 가격으로 마진
        all_marg += margin                          # 마진 총합

    print('#{} {}'.format(t, all_marg))