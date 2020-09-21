def matrixMult(A):
    row=len(A)
    col=len(A[0])
    B = [[0 for row in range(row)]for col in range(col)]
    for i in range(row):
        for j in range(col):
            B[j][i]=A[i][j]
    return B

def checkleft(line,L):
    visitied = [0]*len(line)
    check=[0]*len(line)
    count = 1
    while True:
        if 0 not in visitied:
            break
        else:
            now = visitied.index(0)
            visitied[now] = 1
            if now != len(visitied)-1:
                if line[now+1] == line[now]:
                    count +=1
                    continue
                else:
                    if line[now]-line[now+1]==1:
                        temp = line[now+1]
                        newcount = 0
                        for i in range(now+1,len(line)):
                            if line[i]==temp:
                                newcount+=1
                                visitied[i] = 1
                            else:
                                if newcount>=L:
                                    if check[now:now+L]!=1:
                                        for j in range(now+1,now+1+L):
                                            check[j]=1
                                        count=1
                                        break
                                    else:
                                        return False
                        else:
                            return False
                    elif line[now]-line[now+1]==-1:
                        if count >=L:
                            if check[now:now+L]!=1:
                                for j in range(now,now+L):
                                    check[j]=1
                                count = 1
                                continue
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
    return True



def solution(MAPS, N, L):
    answer = 0
    for i in range(N):
        if checkleft(MAPS[i],L):
            answer+=1
    
    MAPS=matrixMult(MAPS)
    
    for i in range(N):
        if checkleft(MAPS[i],L):
            answer+=1
    
    return answer


def main():
    N, L = map(int,input().split())
    MAPS = list()
    for _ in range(N):
        line = list(map(int,input().split()))
        MAPS.append(line)
    
    print(solution(MAPS, N, L))

main()