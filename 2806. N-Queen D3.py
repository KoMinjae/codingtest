def solution(N):
    count = 0
    if N == 1:
        return 1
    elif N == 2:
        return 0
    else:
        stack=list()
        for i in range(1,N+1):
            stack.append(([i],1))
            while stack:
                queens, row = stack.pop()
                if len(queens)==N:
                    count+=1
                else:
                    check=[i for i in range(1,N+1)]
                    for j in range(row):
                        for queen in range(1,N+1):
                            if queen != queens[j]:
                                if queen==queens[j]-j+row or queen==queens[j]+j-row:
                                    if queen in check:
                                        check.remove(queen)
                            else:
                                if queen in check:
                                    check.remove(queen)
                    if check:
                        for i in check:
                            stack.append((queens+[i], row+1))

    return count


def main():
    T = int(input())
    for test_case in range(1,T+1):
        N = int(input())
        print("#{} {}".format(test_case, solution(N)))

main()