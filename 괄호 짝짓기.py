
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    N=int(input())
    lists=list(input())
    checklist=list()
    answer = 1
    for i in range(N):
        if lists[i] == ")":
            if "(" in checklist:
                checklist.pop(checklist.index("("))
            else : 
                answer = 0
                break
        elif lists[i] == ">" :
            if "<" in checklist:
                checklist.pop(checklist.index("<"))
            else : 
                answer = 0
                break
        elif lists[i] == "}" :
            if "{" in checklist:
                checklist.pop(checklist.index("{"))
            else : 
                answer = 0
                break
        elif lists[i] == "]" :
            if "[" in checklist:
                checklist.pop(checklist.index("["))
            else : 
                answer = 0
                break
        else:
            checklist.append(lists[i])
    print("#"+str(test_case),answer)
    # ///////////////////////////////////////////////////////////////////////////////////
