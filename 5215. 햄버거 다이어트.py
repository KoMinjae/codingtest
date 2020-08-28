#시간초과뜸
def solution(products,L):
    stack=list()
    maxfla=0
    numlist = [i for i in range(len(products))]
    maxcal=0
    idx = 0
    stack.append(([],0,0,idx))

    while stack:
        menulist , flavor, cal, idx = stack.pop()
        if cal > L:
            continue
        if maxfla <= flavor :
            maxfla = flavor
        if idx >= len(products):
                continue
        for i in range(2):
            if i == 0:
                if cal+products[idx][1]<=L:
                    stack.append((menulist+[idx],flavor+products[idx][0],cal+products[idx][1],idx+1))
            elif i == 1:
                stack.append((menulist,flavor,cal,idx+1))
    return maxfla
def main():
    T=int(input())
    for test_case in range(1,T+1):
        N, L = map(int,input().split())
        products=list()
        for i in range(N):
            product = list(map(int,input().split()))
            products.append(product)
        if len(products) == 0:
            print("#{} {}".format(test_case, 0))
        else:
            print("#{} {}".format(test_case, solution(products,L)))

main()