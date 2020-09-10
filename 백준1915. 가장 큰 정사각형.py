def solution(N,M,MAPS):
    answer = 1
    for i in range(1,N):
        for j in range(1,M):
            if MAPS[i][j] == 1:
                MAPS[i][j] = min(MAPS[i-1][j-1],MAPS[i][j-1],MAPS[i-1][j])+1
                answer = max(MAPS[i][j], answer)
    
    return answer**2
def main():
    N, M = map(int,input().split())
    MAPS = list()
    check=False
    for i in range(N):
        line = list(map(int,list(input())))
        if 1 in line:
            check=True
        MAPS.append(line)
    if check == False:
        print(0)
    else:
        print(solution(N, M, MAPS))

main()
