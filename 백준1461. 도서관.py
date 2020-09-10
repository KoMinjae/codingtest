def solution(N,M,booklist):
    booklist.sort()
    leftlist=list()
    rightlist=list()
    sumlen=0
    highlen = max(max(booklist),min(booklist)*-1)
    for i in booklist:
        if i < 0:
            leftlist.append(i*-1)
        else:
            rightlist.append(i)
    leftlist.sort()
    rightlist.sort()
    while leftlist:
        sumlen+=leftlist[-1]
        for i in range(M):
            if leftlist:
                leftlist.pop()
    while rightlist:
        sumlen+=rightlist[-1]
        for i in range(M):
            if rightlist:
                rightlist.pop()

    sumlen=sumlen*2-highlen

    return sumlen

def main():
    N, M = map(int, input().split())
    booklist = list(map(int, input().split()))
    print(solution(N,M,booklist))

main()