"""7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
def solution(MAPS,N):
    stack=list()
    visitied=list()
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    count=1
    answers=list()
    for j in range(N):
        for k in range(N):
            if MAPS[j][k] == 1:
                start=(j,k)
                count+=1
                stack.append((j,k))
                visitied.append((j,k))
                MAPS[j][k]=count
                answer=1
                while stack:
                    x,y = stack.pop()
                    for i in range(4):
                        if 0<=dx[i]+x<N and 0<=dy[i]+y<N and (dx[i]+x,dy[i]+y) not in visitied:
                            if MAPS[dx[i]+x][dy[i]+y] != 0:
                                stack.append((dx[i]+x,y+dy[i]))
                                visitied.append((dx[i]+x,dy[i]+y))
                                MAPS[dx[i]+x][dy[i]+y]=count
                                answer+=1
                answers.append(answer)
    answers.sort()
    return count, answers
def main():
    N = int(input())
    MAPS=list()
    for i in range(N):
        line = list(map(int,list(input())))
        MAPS.append(line)
    count , answer = (solution(MAPS,N))
    print(count-1)
    for i in answer:
        print(i)
main()