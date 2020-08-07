def makemap(maps):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j]=='.':
                count = 0
                if i-1>=0:
                    if maps[i-1][j] == "*":
                        count+=1
                    if j-1 >= 0:
                        if maps[i-1][j-1] == "*":
                            count+=1
                    if j+1<len(maps[i]):
                        if maps[i-1][j+1] == "*":
                            count+=1
                if j+1<len(maps[i]):
                    if maps[i][j+1] == "*":
                        count+=1
                if j-1>=0:
                    if maps[i][j-1] == "*":
                        count+=1
                if i+1<len(maps):
                    if maps[i+1][j] == "*":
                        count+=1
                    if j-1>=0:
                        if maps[i+1][j-1] == "*":
                            count+=1
                    if j+1<len(maps[i]):
                        if maps[i+1][j+1] == "*":
                            count+=1
                maps[i][j]=count
    return solution(maps)
def solution(maps):
    zeroidx=[]
    while True:
        for i in range(maps):
            if 0 in maps[i]:
                if (i,maps[i].index(0)) not in zeroidx:
                    zeroidx.append((i,maps[i].index(0)))
                    break
        if i-1>=0:
            if maps[i-1][j] == "*":
                    count+=1
            if j-1 >= 0:
                if maps[i-1][j-1] == "*":
                        count+=1
            if j+1<len(maps[i]):
                if maps[i-1][j+1] == "*":
                        count+=1
            if j+1<len(maps[i]):
                if maps[i][j+1] == "*":
                    count+=1
            if j-1>=0:
                if maps[i][j-1] == "*":
                    count+=1
            if i+1<len(maps):
                if maps[i+1][j] == "*":
                    count+=1
                if j-1>=0:
                    if maps[i+1][j-1] == "*":
                        count+=1
                if j+1<len(maps[i]):
                    if maps[i+1][j+1] == "*":
                        count+=1
        
makemap([['.','.','*'],['.','.','*'],['*','*','.']])