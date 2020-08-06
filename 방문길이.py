import copy
def solution(dirs):
    answer = 0
    coord=list()
    coord.append(0)
    coord.append(0)
    movehistory=list()
    for i in dirs:
        newcoord=movearrow(coord,i)
        if (coord,newcoord) not in movehistory and coord!=newcoord:
            movehistory.append((coord,newcoord))
            movehistory.append((newcoord,coord))
        coord=newcoord

    return (len(movehistory)//2)
def movearrow(position,move):
    getcoord = copy.copy(position)
    if move == "U":
        if position[1]!=5:
            getcoord[1]+=1
    elif move == "D":
         if position[1]!=-5:
             getcoord[1]-=1
    elif move == "L":
        if position[0]!=-5:
            getcoord[0]-=1
    elif move == "R":
        if position[0]!=5:
            getcoord[0]+=1
    return getcoord


solution("LULLLLLLU	")