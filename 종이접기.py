def solution(n):
    answer = list()
    answer.append([0])
    answer.append([0,0,1])
    answer.append([0,0,1,0,0,1,1])
    if n > 3:
        for i in range(3,n):
            temp = answer[i-1]
            reversetemp = reversed(temp)
            addlist=list()
            for j in reversetemp:
                if j == 0:
                    addlist.append(1)
                else:
                    addlist.append(0)
            answer.append(
    return answer[n-1]
solution(4)