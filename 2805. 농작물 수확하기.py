def solution(MAPS):
    temp=1
    result=0
    for i in range(len(MAPS)//2):
        for j in range((len(MAPS)-temp)//2):
            MAPS[i].pop(0)
        for j in range(temp):
            result+=MAPS[i].pop(0)
        temp+=2
    result+=sum(MAPS[len(MAPS)//2])
    for i in range(len(MAPS)//2+1,len(MAPS)):
        temp-=2
        for j in range((len(MAPS)-temp)//2):
            MAPS[i].pop(0)
        for j in range(temp):
            result+=MAPS[i].pop(0)

    return result
def main():
    T=int(input())
    for test_case in range(1,T+1):
        N = int(input())
        MAPS=list()
        for i in range(N):
            lines = list(map(str,input()))
            intlines=[int(i) for i in lines]
            MAPS.append(intlines)
        print("#{} {}".format(test_case, solution(MAPS)))

main()