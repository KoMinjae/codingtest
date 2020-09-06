import copy
def solution(MAPS,N):
    solMap = copy.deepcopy(MAPS)
    solMap[0] = MAPS[0]
    for i in range(1,N):
        maxlen=len(MAPS[i])
        for j in range(maxlen):
            if j == 0 :
                solMap[i][j] = solMap[i-1][j]+MAPS[i][0]
            elif j == maxlen-1:
                solMap[i][j] = solMap[i-1][j-1]+MAPS[i][maxlen-1]
            else:
                solMap[i][j] = max(solMap[i-1][j-1],solMap[i-1][j])+MAPS[i][j]
    return max(solMap[-1])
def main():
    N = int(input())
    MAPS=list()
    for i in range(N):
        line = list(map(int,input().split()))
        MAPS.append(line)
    print(solution(MAPS,N))
main()
    