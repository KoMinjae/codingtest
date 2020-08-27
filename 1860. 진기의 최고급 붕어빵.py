def solution(cus,M,K):
    count=0
    time = 0
    while cus:
        if time != 0:
            if time % M == 0:
                count+=K
        if cus[0] <=time:
            if count!=0:
                cus.pop(0)
                count-=1
            else:
                return "Impossible"
        time+=1
    return "Possible"

def main():
    T=int(input())
    for test_case in range(1,T+1):
        N,M,K = map(int,input().split())
        custom=list(map(int,input().split()))
        custom.sort()
        print("#{} {}".format(test_case, solution(custom,M,K)))
main()

