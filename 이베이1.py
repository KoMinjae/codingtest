#맞음
def solution(N, simulation_data):
    answer = 0
    stack=list()
    time = 0
    count=0
    idxlist=list()
    while simulation_data:
        count=0
        idxlist=list()
        for i in range(len(simulation_data)):
             if simulation_data[i][0] <=time:
                if len(idxlist)!=N:
                    idxlist.append(i)
        for i in range(len(idxlist)):
            if len(stack)!=N:
                stack.append(simulation_data.pop(0))
        if simulation_data:
            if time>=simulation_data[0][0]:
                for i in simulation_data:
                    if i[0] <= time:
                        count+=1
                answer+=count
        if len(stack)!=0:
            for i in range(len(stack)):
                if stack[i][1] != 0:
                    stack[i][1] -=1
        for j in range(len(stack)-1,-1,-1):
            if stack[j][1]==0:
                stack.pop(j)
                   
        time +=1
        
    return answer

solution(2, [[0, 3],[0,1], [0, 5],[3,2], [4, 2], [5, 3],[10,11]])