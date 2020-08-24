def solution(N,M):
    numlist = list()
    for i in str(N):
        numlist.append(i)
    stack=list()
    stack.append((numlist,M))
    check = {}
    maxs = 0
    while stack:
        numlists , count = stack.pop(0)
        if count == 0 :
            if maxs < int(''.join(numlists)):
                maxs=int(''.join(numlists))
                continue
            else:
                continue
        for i in range(len(numlist)):
            for j in range(i+1, len(numlist)):
                numlists[i], numlists[j] = numlists[j], numlists[i]
                result = ''.join(numlists)
                if check.get((''.join(numlists),count-1),1):
                    check[(''.join(numlists),count-1)]= 0
                    stack.append((list(result), count-1))
                numlists[i], numlists[j] = numlists[j], numlists[i]

    return maxs
def main():
    T = int(input())

    for test_case in range(1,T+1):
        N , M = map(int,input().split())
        print("#{} {}".format(test_case, solution(N,M)))
main()
