from itertools import combinations

def solution(Numlist, M):
    sooyeol=list()
    count=0
    if len(Numlist) == 1:
        if Numlist[0] == M:
            return 1
        else:
            return 0
    else:
        for i in range(1,len(Numlist)+1):
            for comb in combinations(Numlist,i):
                if sum(comb)==M:
                    count+=1
        return count

def main():
    T=int(input())
    for test_case in range(1,T+1):
        N, M= map(int,input().split())
        Numlist = list(map(int,input().split()))

        print("#{} {}".format(test_case, solution(Numlist, M)))


main()