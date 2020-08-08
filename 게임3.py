import copy

def solution(board):
    answer = 0
    maps=copy.deepcopy(board)
    for i in range(len(maps)):
        for j in range(len(maps)):
            answer=answer + move(i,j,maps)
    if answer == 0:
        return -1
    return answer//2

def move(x,y,maps):
    count=0
    mx=[1,-1,0,0]
    my=[0,0,1,-1]
    for i in range(4):
        dx=x+mx[i]
        dy=y+my[i]
        if -1<dx<len(maps) and -1<dy<len(maps):
            if check(dx,dy,x,y,maps):
                count+=1
    return count

def check(dx,dy,x,y,maps):
    checkmap=copy.deepcopy(maps)
    temp=0
    checkmap[x][y],checkmap[dx][dy]=checkmap[dx][dy],checkmap[x][y]
    for i in range(len(checkmap)):
        temp = checkmap[i][0]
        count=0
        for j in range(len(checkmap)):
            if checkmap[i][j] == temp:
                count+=1
                if count==3:
                    return True
            else:
                temp = checkmap[i][j]
                count=1

    for i in range(len(checkmap)):
        temp=checkmap[0][i] 
        count = 0
        for j in range(len(checkmap)):
            if checkmap[j][i] ==temp:
                count+=1
                if count==3:
                    return True
            else:
                temp = checkmap[j][i]
                count=1
    return False

solution([[1,1,4,3],[3,2,1,4],[3,1,4,2],[2,1,3,3]])