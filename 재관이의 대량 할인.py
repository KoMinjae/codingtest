T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N= int(input())
    pricelist = list(map(int, input().split()))
    pricelist.sort()
    temp=0
    answer=0
    for i in range(len(pricelist)-1,-1,-1):
        temp+=1
        if temp ==3 :
            answer+=pricelist.pop()
            answer+=pricelist.pop()
            pricelist.pop()
            temp=0
    if temp ==2:
        answer+=pricelist.pop()
        answer+=pricelist.pop()
    elif temp == 1:
        answer+=pricelist.pop()
    print('#{} {}'.format(test_case, answer))
    # ///////////////////////////////////////////////////////////////////////////////////
