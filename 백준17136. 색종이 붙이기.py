def solution(MAPS):
    maxnum = 0
    paper = [5]*5
    count = 0
    while True:
        for i in range(1,10):
            for j in range(1,10):
                if MAPS[i-1][j-1]!=0 and MAPS[i][j-1] !=0 and MAPS[i-1][j] != 0 :
                    MAPS[i][j]=min(MAPS[i-1][j-1], MAPS[i][j-1], MAPS[i-1][j])+1
                    if MAPS[i][j] > maxnum:
                        maxnum = MAPS[i][j]
        if maxnum > 5:
            maxnum = 5
        deletenum = maxnum
        for i in range(10):
            for j in range(10):
                if MAPS[i][j] == maxnum:
                    if paper[maxnum-1]!=0:
                        for t in range(deletenum):
                            for x in range(deletenum):
                                MAPS[i-(deletenum-1)+t][j-x] = 0
                        count+=1
                        for i in range(1,10):
                            for j in range(1,10):
                                if MAPS[i-1][j-1]!=0 and MAPS[i][j-1] !=0 and MAPS[i-1][j] != 0 :
                                    MAPS[i][j]=min(MAPS[i-1][j-1], MAPS[i][j-1], MAPS[i-1][j])+1
                                    if MAPS[i][j] > maxnum:
                                        maxnum = MAPS[i][j]
                        if maxnum > 5:
                            maxnum = 5
                    else:
                        deletenum-=1

        if maxnum not in MAPS:
            maxnum-=1

    return 0

def main():
    MAPS=list()
    for i in range(10):
        line = list(map(int,input().split()))
        MAPS.append(line)

    print(solution(MAPS))

main()