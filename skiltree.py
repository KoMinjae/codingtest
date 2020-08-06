def check(p):
    stack = list(p)
    checkstack=[]
    for i in stack:
        if i == "(":
            checkstack.append(i)
        elif i == ")" and len(checkstack)!=0:
            checkstack.pop()
    if len(checkstack)==0:
        return True
    else:
        return False
def uvdiv(p):
    stack = list(p)
    ustack=[]
    vstack=[]
    ustack.append(stack.pop(0))
    lcount = ustack.count("(")
    rcount = ustack.count(")")
    for i in stack:
        if lcount != rcount:
            ustack.append(i)
            lcount = ustack.count("(")
            rcount = ustack.count(")")
        else:
            vstack.append(i)
    return ustack, vstack

def solution(p):
    stack = list(p)
    emptystack=[]
    if check(p) == True:
        return p
    ustack, vstack = uvdiv(p)
    if check(ustack) == True:
        answer.append(ustack)
        solution(vstack)
    elif check(ustack) == False:
        emptystack.append("(")
        emptystack.append(solution(vstack))
        emptystack.append(")")
        answer.append(emptystack)
    return p
print(solution("()))((()"))