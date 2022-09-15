import sys
sys.stdin = open('input.txt','r')
bun = int(input())
# 길이 반환하는 함수 생성
def ll(l) :
    cnt = 0
    for i in l :
        cnt += 1
    return cnt
for he in range(1,bun+1) :
    a = list(str(input()))
    b = list(str(input()))
    alph_max = 0
    # a리스트의 단어
    for i in range(ll(a)):
        alph = 0
        # b리스트의 단어
        for j in range(ll(b)):
            # a, b 리스트의 단어 찾아서 
            if a[i] == b[j]:
				# 단어별 개수 확인
                alph += 1
				# 최대값 찾기
                if alph_max < alph :
                    alph_max = alph
    print('#{} {}'.format(he, alph_max))