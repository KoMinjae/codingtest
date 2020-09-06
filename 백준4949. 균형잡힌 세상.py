def check(strlist):
    newlist=list()
    for i in range(len(strlist)):
        if strlist[i]=="(":
            newlist.append("(")
        elif strlist[i]=="[":
            newlist.append("[")
        elif strlist[i]==")":
            if newlist:
                if newlist[-1]=="(":
                    newlist.pop()
                else:
                    return "no"
            else:
                return "no"
        elif strlist[i]=="]":
            if newlist:
                if newlist[-1]=="[":
                    newlist.pop()
                else:
                    return "no"
            else:
                return "no"
    if newlist==[]:
        return "yes"
    else:
        return "no"

strlist = ""
while True:
    strlist = input()
    if strlist == ".":
        break
    print(check(strlist))