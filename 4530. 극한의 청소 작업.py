##4하나 없는거니까 9 진법으로 바꿔서 풀면됨

def makenine(NUMS):
    sum=0
    n=len(NUMS)
    for idx,num in enumerate(NUMS):
        j=int(num)
        if j<4:
            sum+=j*9**(n-1-idx)
        else:
            sum+=(j-1)*9**(n-1-idx)
    return sum
def main():
    T = int(input())
    answer = 0
    building=list()
    for test_case in range(1,T+1):
        N,M = map(str, input().split())
        if N[0]=='-' and M[0]=='-':
            answer=(makenine((N[1:])))-(makenine((M[1:])))
        elif N[0]=='-' and M[0]!='-':
            answer=(makenine((N[1:])))+(makenine((M[:])))-1
        else:
            answer=(makenine((M[:])))-(makenine((N[:])))
        print("#{} {}".format(test_case, answer))
main()