def solution(stats):
    rate=list()
    for i,x in enumerate(stats):
        numcount=0
        for num in x:
            if num=="1":
                numcount+=1
        rate.append(numcount/len(x))
    return min(rate)

print(solution(["1222","1122","1222"]))