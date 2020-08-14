def solution(n,maps):
    start=None
    goal=None
    answer=list()
    stack = list()
    mx = [0,1]
    my = [1,0]
    cx,cy=0,0
    
    for i in range(len(maps)):
        for x in range(len(maps)):
            if maps[i][x]!=0:
                    start = (i,x)
                    stack.append((start,0,0))
                    maxcx=0; maxcy=0
                    while stack:
                        coord,cx,cy = stack.pop()
                        if maxcx<cx:
                            maxcx=cx
                        if maxcy<cy:
                            maxcy=cy
                        x=coord[0]; y=coord[1]
                        maps[x][y]=0
                        for j in range(2):
                            dx=x+mx[j]; dy = y+my[j]
                            if -1<dx<n and -1<dy<n and maps[dx][dy] != 0:
                                if j == 0:
                                    stack.append(((dx,dy),cx+1,cy))
                                elif j == 1:
                                    stack.append(((dx,dy),cx,cy+1))
                    answer.append((maxcy+1,maxcx+1))
    answer.sort(key = lambda x:(x[0]*x[1],x[0]))
    result=""
    for i in answer:
        result = result+str(i[0])+" "+str(i[1])+" "
    return str(len(answer))+" "+result
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T= int(input())
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N=int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    print("#"+str(test_case),solution(N,maps))
    # ///////////////////////////////////////////////////////////////////////////////////
