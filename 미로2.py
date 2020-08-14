def solution(start,goal,maps):
    mx = [1,-1,0,0]
    my = [0,0,1,-1]
    visited=[]
    stack=list()
    stack.append(start)
    while stack:
        x,y =stack.pop(0)
        for i in range(4):
            if (x,y) == goal:
                return 1
            dx = x+mx[i]
            dy = y+my[i]
            if -1<dx<100 and -1<dy<100 and maps[dx][dy]!=1 and (dx,dy) not in visited:
                visited.append((dx,dy))
                stack.append((dx,dy))
    return 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    input()
    maps=list()
    start=None
    goal=None
    for i in range(100):
        line = list(map(int,list(input().strip())))
        maps.append(line)
        if 2 in line:
            start = (i,line.index(2))
        if 3 in line:
            goal = (i,line.index(3))
    print("#"+str(test_case),solution(start,goal,maps))
    # ///////////////////////////////////////////////////////////////////////////////////
