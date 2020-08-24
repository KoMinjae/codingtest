def solution(towers):
    lhigh = 0
    rhigh = 0
    count = 0
    for i in range(2,len(towers)-2):
        lhigh=max(towers[i-2],towers[i-1])
        rhigh=max(towers[i+1],towers[i+2])
        if towers[i] > lhigh and towers[i] > rhigh:
            count += towers[i] - max(lhigh,rhigh)
    
    return count

def main():
    for test_case in range(1,11):
        N = int(input())
        towers = list(map(int,input().split()))
        
        print("#{} {}".format(test_case, solution(towers)))


main()