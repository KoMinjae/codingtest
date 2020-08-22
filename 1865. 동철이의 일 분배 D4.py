###가지치기를 이용한 DFS
###DP로도 풀 수 있을것 같은데..

import copy
def solution(MAPS):
    answer=0.0
    maxs=0.0
    subresult=0
    stack=list()
    DP=copy.deepcopy(MAPS)
    idx = 0
    stack.append((idx , 1.0, []))
    while stack:
        idx , result, visitied = stack.pop()
        if result<=maxs:
            continue
        if idx == len(DP):
            if maxs<result:
                maxs=result
                continue
            else:
                continue
        for j in range(len(DP[idx])):
            if j not in visitied:
                stack.append((idx+1,(DP[idx][j]*result*0.01),visitied+[j]))

    return maxs*100

def main():
    T = int(input())
    for test_case in range(1,T+1):
        N = int(input())
        MAPS=list()
        for i in range(N):
            line = list(map(int,input().split()))
            MAPS.append(line)
        print('#{} {:.6f}'.format(test_case, solution(MAPS)))

main()