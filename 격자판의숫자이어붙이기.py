def solution(N):
    answer=set()
    visited=list()
    #격자판 시작 위치
    for i in range(4):
        for j in range(4):
            num=""
            visited=list()
            visited.append((i,j,num))
            #dfs
            while visited:
                dx,dy,num = visited.pop()
                #조건 성립
                if len(num)==7:
                    answer.add(num)
                else:
                    for x in range(4):
                        if x == 0:
                            if dx+1<=3:
                                visited.append((dx+1,dy,num+N[dx+1][dy]))
                        elif x == 1:
                            if dx-1>=0:
                                visited.append((dx-1,dy,num+N[dx-1][dy]))
                        elif x == 2:
                            if dy+1<=3:
                                visited.append((dx,dy+1,num+N[dx][dy+1]))
                        elif x == 3:
                            if dy-1>=0:
                                visited.append((dx,dy-1,num+N[dx][dy-1]))
    return len(answer)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=[list(map(str,input().split())) for _ in range(4)]
    print("#"+str(test_case),solution(N))
