def generateset(inputlist):
    answer = []
    for i in inputlist:
        if i not in answer:
            answer.append(i)
    print(answer)
generateset([1,2,3,2,1])