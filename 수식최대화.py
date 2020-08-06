from itertools import permutations
def opeations(num1,num2,oper):
    if oper == "+":
        return num1+num2
    elif oper == "-":
        return num1-num2
    elif oper == "*":
        return num1*num2
def solution(expression):
    prefix = list()
    stack = list(expression)
    numstack = list()
    notnumstack=list()
    answer = list()
    oplist = list(permutations(["+","-","*"],3))
    for i in oplist:
        number=""
        for k in stack:
            if k.isdigit():
                number+=k
            else :
                numstack.append(number)
                notnumstack.append(k)
                number=""
        numstack.append(number)
        for j in i:
            while j in notnumstack:
                idx = notnumstack.index(j)
                notnumstack.pop(idx)
                opresult = opeations(int(numstack[idx]),int(numstack[idx+1]), j)
                numstack.pop(idx)
                numstack.pop(idx)
                numstack.insert(idx,str(opresult))
        answer.append(abs(int(numstack[0])))
        numstack=list()
    return max(answer)



solution("100-200*300-500+20")