def matrixMult(MAPS):
    row=len(MAPS)
    col=len(MAPS[0])
    B = [[0 for row in range(row)]for col in range(col)]
    for i in range(row):
        for j in range(col):
            B[j][i]=MAPS[i][j]
    return B

def solution(MAPS,N):
    count=0
    for i in range(8):
        for j in range(8-N+1):
            if j == 0:
                a= MAPS[i][N-1::-1]
            else:
                a= MAPS[i][j+N-1:j-1:-1]
            if MAPS[i][j:j+N] == a:
                count+=1
    
    TMAPS = matrixMult(MAPS)
    
    for i in range(8):
        for j in range(8-N+1):
            if j == 0:
                a= TMAPS[i][N-1::-1]
            else:
                a= TMAPS[i][j+N-1:j-1:-1]
            if TMAPS[i][j:j+N]==a:
                count+=1

    return count



def main():
    for test_case in range(1,11):
        N = int(input())
        MAPS=list()
        for i in range(8):
            lines=list(input())
            MAPS.append(lines)
        print("#{} {}".format(test_case,solution(MAPS,N)))

main()