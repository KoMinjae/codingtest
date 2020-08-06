def solution(s):
    if len(s)==1:
        return 1
    answer = 0
    temp = ""
    answerlist=list()
    count=1
    lenlist = list()
    lenlist.append(len(s))
    for i in range(1,len(s)//2+1):
        temp=s[:i]
        for j in range(i,len(s)+1,i):
            if s[j:j+i] == temp:
                count+=1
            else :
                if count==1:
                    answerlist.append(temp)
                else :
                    answerlist.append(str(count)+temp)
                temp=s[j:j+i]
                count=1
        if len(temp)<j:
            answerlist.append(temp)
        lenlist.append(len("".join(answerlist)))
        answerlist=list()
        answer = min(lenlist)
    return answer

print(solution("a"))