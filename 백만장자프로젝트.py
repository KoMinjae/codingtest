def solution(value):
    answer=0
    while True:
        maxcost = max(value)
        maxcostidx = value.index(max(value))
        if maxcostidx == len(value)-1:
            for i in value:
                answer += maxcost-i
            return answer
        elif maxcostidx == 0:
            value=value[1::]
            continue
        else:
            for i in range(0,maxcostidx):
                answer+= maxcost-value[i]
        value=value[maxcostidx+1::]
#뒤에서부터 탐색해야 시간초과 안뜸
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N=int(input())
    pricelist = list(map(int,input().split()))
    print("#"+str(test_case),solution(pricelist))
    # ///////////////////////////////////////////////////////////////////////////////////
