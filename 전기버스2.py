def solution(N,bp):
    answer = list()
    battery = bp[0]
    stack=list()
    stack.append((1,battery,0))
    mintemp=999999
    while stack:
        position, nowbattery, time = stack.pop(0)
        #백트래킹 조건
        if time <= mintemp:
            if position == N:
                answer.append(time)
                if mintemp>time:
                    mintemp=time
            else:
                for i in range(1,nowbattery+1):
                        if position+i>=N:
                            stack.append((N,0,time))
                        else:
                            stack.append((position+i,bp[position+i-1],time+1))
    return min(answer)
print(solution(10, [2, 1, 3, 2, 2, 5, 4, 2, 1]))