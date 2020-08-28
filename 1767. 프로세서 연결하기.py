import copy
def solution(N,MAPS,core):
    stack=list()
    visit=list()
    stack.append((0,0,0,copy.deepcopy(MAPS)))
    minlen=9999
    maxcore=0
    answer=list()
    while stack:
        idx, corecount, linelen, copymap = stack.pop()
        answer.append((corecount,linelen))
        if idx==len(core):
            continue
        nowcore = core[idx]
        checks=0
        for i in range(4):
            newcopymap=copy.deepcopy(copymap)
            #오른쪽
            if i == 0:
                if 1 not in newcopymap[nowcore[0]][nowcore[1]+1:]:
                    for j in range(nowcore[1]+1,N):
                        newcopymap[nowcore[0]][j]=1
                    stack.append((idx+1,corecount+1,linelen+N-nowcore[1]-1,newcopymap))
                    checks+=1
            #왼쪽
            elif i == 1:
                if 1 not in newcopymap[nowcore[0]][:nowcore[1]]:
                    for j in range(0,nowcore[1]):
                        newcopymap[nowcore[0]][j]=1
                    stack.append((idx+1,corecount+1,linelen+nowcore[1],newcopymap))
                    checks+=1
            #위
            elif i == 2:
                check=True
                for j in range(nowcore[0]):
                    if newcopymap[j][nowcore[1]] == 1:
                        check=False
                        break
                if check==True:
                    for z in range(0,nowcore[0]):
                        newcopymap[z][nowcore[1]]=1
                    stack.append((idx+1,corecount+1,linelen+nowcore[0],newcopymap))
                    checks+=1
            #아래
            elif i == 3:
                check=True
                for j in range(nowcore[0]+1,N):
                    if newcopymap[j][nowcore[1]] == 1:
                        check=False
                        break
                if check==True:
                    for z in range(nowcore[0]+1,N):
                        newcopymap[z][nowcore[1]]=1
                    stack.append((idx+1,corecount+1,linelen+N-nowcore[0]-1,newcopymap))
                    checks+=1
        if checks == 0:
            stack.append((idx+1,corecount,linelen,newcopymap))
    answer.sort(key = lambda x:(x[0],-x[1]))
    return answer[-1][1]
def main():
    T=int(input())
    for test_case in range(1,T+1):
        MAPS=list()
        N=int(input())
        core = list()
        for i in range(N):
            line=list(map(int,input().split()))
            if 1 in line:
                for j in range(len(line)):
                    if line[j] == 1:
                        if i != 0 and i != N and j != 0 and j != N:
                            core.append((i,j))
            MAPS.append(line)
        print("#{} {}".format(test_case, solution(N,MAPS,core)))

main()