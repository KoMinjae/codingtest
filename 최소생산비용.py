def solution(N,MAPS):
    stack=list()
    answer=list()
    minscore=99999
    for i in range(N):
        stack.append((i,[i],MAPS[0][i],1))
        while stack:
            position, visited, score, idx=stack.pop()
            #백트래킹 조건
            if score>minscore:
                continue
            else:
                if len(visited)==N:
                    if minscore>score:
                        answer.append(score)
                        minscore=score
                    continue
                else:
                    for j in range(N):
                        if j not in visited:
                            stack.append((j,visited+[j],score+MAPS[idx][j],idx+1))
    return min(answer)
solution(3,[[73, 21, 21,],
[11, 59, 40,],
[24, 31, 83]])