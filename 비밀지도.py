def solution(n, arr1, arr2):
    answer = []
    maprow=""
    firstmap=list()
    nonob1=list()
    nonob2=list()
    secondmap=list()
    for i in arr1:
        firstmap.append(bin(i))
    for i in arr2:
        secondmap.append(bin(i))
    for i in firstmap:
        abc=i[2:]
        nonob1.append(abc)
    for i in secondmap:
        abc=i[2:]
        nonob2.append(abc)
    for i in range(0,len(nonob1)):
        while len(nonob1[i])!=len(arr1):
            nonob1[i]="0"+nonob1[i]
    for i in range(0,len(nonob2)):
        while len(nonob2[i])!=len(arr1):
            nonob2[i]="0"+nonob2[i]
    for i in range(0,len(nonob1)):
        maprow=""
        for j in range(0,len(nonob1[i])):
            if nonob1[i][j]=="0" and nonob2[i][j]=="0":
                maprow=maprow+" "
            else:
                maprow=maprow+"#"
        answer.append(maprow)
    return answer



solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])