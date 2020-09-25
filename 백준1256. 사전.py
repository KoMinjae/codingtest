from itertools import permutations
def main():
    numlist=list()
    N, M, K = map(int,input().split())
    for i in range(N):
        numlist.append("a")
    for i in range(M):
        numlist.append("z")
    answers = list(permutations(numlist,r=4))
    answer = list()
    for i in answers:
        if i not in answer:
            answer.append(i)
    print(''.join(answer[K-1]))

main()