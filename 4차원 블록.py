def solution(m, n, board):
    answer = 0
    maps=[[j for j in i]for i in board]
    count=0
    while True:
        maps, count=blockDelete(maps)
        if count == 0:
            break
        answer+=count
        Blockdown(maps)
    return answer

def Blockdown(Map):
    for i in range(len(Map)-1,0,-1):
        for j in range(0,len(Map[i])):
            if Map[i][j] == '0':
                count = i-1
                while count>=0:
                    if Map[count][j] !='0':
                        Map[i][j] = Map[count][j]
                        Map[count][j] = '0'
                        count=-1
                    else :
                        count-=1
    return Map
def blockDelete(Map):
    checkboard=set()
    DeleteCount=0
    for i in range(len(Map)-1,0,-1):
        for j in range(len(Map[i])-1,0,-1):
            if Map[i][j]==Map[i][j-1] and Map[i][j]==Map[i-1][j-1]and Map[i][j]==Map[i-1][j] and Map[i][j]!="0":
                checkboard.add((i,j))
                checkboard.add((i,j-1))
                checkboard.add((i-1,j))
                checkboard.add((i-1,j-1))
    DeleteCount=len(checkboard)
    for i in checkboard:
        Map[i[0]][i[1]]="0"
    return Map,DeleteCount
solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])