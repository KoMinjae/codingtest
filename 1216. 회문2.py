def matrixMult(MAPS):
    row=len(MAPS)
    col=len(MAPS[0])
    B = [[0 for row in range(row)]for col in range(col)]
    for i in range(row):
        for j in range(col):
            B[j][i]=MAPS[i][j]
    return B

def solution(MAPS):
    maxlen=0
    for i in range(100):
        for j in range(100):
            temp=0
            while j+temp!=100:
                if j == 0:
                    if temp == 0:
                        a= MAPS[i][j]
                    else:
                        a= MAPS[i][j+temp::-1]
                    if MAPS[i][j:j+temp+1] == a:
                        if len(a)>maxlen:
                            maxlen=len(a)
                else:
                    if temp == 0:
                        a= MAPS[i][j]
                    else:
                        a= MAPS[i][j+temp:j-1:-1]
                    if MAPS[i][j:j+temp+1] == a:
                        if len(a)>maxlen:
                            maxlen=len(a)
                temp+=1
    
    TMAPS = matrixMult(MAPS)
    
    for i in range(100):
        for j in range(100):
            temp=0
            while j+temp!=100:
                if j == 0:
                    if temp == 0:
                        a= TMAPS[i][j]
                    else:
                        a= TMAPS[i][j+temp::-1]
                    if TMAPS[i][j:j+temp+1] == a:
                        if len(a)>maxlen:
                            maxlen=len(a)
                else:
                    if temp == 0:
                        a= TMAPS[i][j]
                    else:
                        a= TMAPS[i][j+temp:j-1:-1]
                    if TMAPS[i][j:j+temp+1] == a:
                        if len(a)>maxlen:
                            maxlen=len(a)
                temp+=1
    return maxlen

def main():
    for test_case in range(1,11):
        N = int(input())
        MAPS=list()
        for i in range(100):
            lines=list(input())
            MAPS.append(lines)
        print("#{} {}".format(test_case,solution(MAPS)))

main()