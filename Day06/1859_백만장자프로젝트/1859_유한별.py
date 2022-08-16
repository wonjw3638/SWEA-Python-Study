# 1859_백만장자 프로젝트
# 2022-08-12

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    sales = list(map(int, input().split()))
    idx = n - 1
    max_sale = sales[idx] # (미래에) 판매한 가격
    revenue = 0

    while idx >= 0 : # 뒤에서부터
        if max_sale < sales[idx] : # 만약 더 비싼 금액이 나오면 앞에서 구매한 것들은 거기서 다 팔렸을 것이므로
            max_sale = sales[idx] 
        revenue += max_sale - sales[idx] # 판매한 가격과 현재 가격의 차이를 더해줌
        idx -= 1
    
    print('#{} {}'.format(tc, revenue))