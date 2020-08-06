def solution(space):
    addr=space[0][0]
    addrlist=list()
    values=0
    while values==0:
        if space[int(addr)+1]=="1":
            values=space[int(addr)+2]
        else:
            addr=space[int(addr)+2]
            addrlist.append(addr)
    answer=list()
    answer.append("0;")
    temp=2
    while addrlist:
        answer.append("0")
        addrlist.pop(0)
        answer.append(str(temp))
        temp+=2
    answer.append("1")
    answer.append(values)
    while len(answer)!=9:
        answer.append("0")
    return answer
aspace= list(input().split())
print(solution(aspace))