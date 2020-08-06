def solution(N,MAPS):
    answer=list()
    stack=list()
    stack.append((0,0,MAPS[0][0]))
    visited=list()
    while stack:
        x,y,nums = stack.pop()
        if x==N-1 and y==N-1:
            answer.append(nums)
        else:
            for i in range(2):
                if i ==0:
                    if x+1<N:
                        stack.append((x+1,y,nums+MAPS[x+1][y]))
                elif i == 1:
                    if y+1<N:
                        stack.append((x,y+1,nums+MAPS[x][y+1]))
    return min(answer)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    N=int(input())
    MAPS=[list(map(int,input().split())) for _ in range(N)]
    print("#"+str(i),solution(N,MAPS))