def solution(N, number):
    answer = -1
    dp=[list() for i in range(8)]
    dp[0]=[N]
    dp[1]=[[N+N,N-N,N*N,N/N,int(str(N)*2)]]
    for i in range(2,8):
        if number == int(str(N)*i):
            return i
    for i in range(2,len(dp)):
        dp[i].append([int(str(N)*(i+1))])
        for j in dp[i-1]:
            for x in j:
                oplist=list()
                oplist.append(x+N)
                oplist.append(x-N)
                oplist.append(x*N)
                if x!=0:
                    oplist.append(x//N)
                dp[i].append(oplist)
                if number in oplist:
                    return i+1
    return answer

print(solution(4,17))