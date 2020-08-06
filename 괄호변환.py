def solution(p):
    answer = ''
    stack = list(p)
    count=1
    rcount=0
    lcount=0
    makeright=""
    if rightsentence(stack)==True:
        return p
    while True:
        if checkbalance(p)!=False:
            u,v=checkbalance(p)
            if rightsentence(u)==True:
                answer+=u
                continue
            else:
                makeright+="("
                p=v
                while True:
                    checkbalance
                rightsentence(v)
    return answer

def checkbalance(s):
    rcount=0
    lcount=0
    balancelist=list()
    for i in range(len(s)):
        if s[i]=="(":
            lcount+=1
        elif s[i]==")":
            rcount+=1
        if lcount==rcount:
            if i+1 >= len(s):
                return s[:i+1], []
            return s[:i+1],s[i+1:]
    else:
        return False
#def makebalance(s):

def rightsentence(s):
    count=1
    while True:
        if count>=len(s):
            return False
        if s[count]==")":
            if s[count-1]=="(":
                s.pop(count)
                s.pop(count-1)
                count=1
            else: 
                count+=1
        else:
            count+=1
        if len(s)==0:
            return True
solution(")(")