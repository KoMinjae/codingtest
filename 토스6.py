def solution(tables):
    first=set()
    left=0
    down=0
    move=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(len(tables)):
        for j in range(len(tables[i])):
            if tables[i][j]=="1":
                first.add(i,j)

    return 0

print(solution([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]))