import math
def solution(escape):
    hallwaylist = [0]*201
    for i in escape:
        if i[0]<i[1]:
            start = i[0]
            end = i[1]
        else:
            start=i[1]
            end = i[0]
        starthall = math.ceil(start/2)
        endhall = math.ceil(end/2)
        for i in range(starthall, endhall+1):
            hallwaylist[i]=hallwaylist[i]+1
    return max(hallwaylist)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    escapes=list()
    num = int(input())
    for i in range(num):
        escapes.append(list(map(int,input().split())))
    print("#"+str(test_case),solution(escapes))
    # ///////////////////////////////////////////////////////////////////////////////////
