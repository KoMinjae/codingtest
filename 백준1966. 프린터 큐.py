for test_case in range(int(input())):
    queue = list()
    N, M = map(int,input().split())
    prior = list(map(int,input().split()))
    for i in range(N):
        queue.append((prior[i],i))
    count = 1
    while queue:
        P, num = queue.pop(0)
        if P == max(prior):
            if num == M:
                print(count)
                break
            else:
                prior.pop(prior.index(max(prior)))
                count+=1
        else:
            queue.append((P,num))
