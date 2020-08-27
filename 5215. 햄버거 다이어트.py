def solution(products,L):
    stack=list()
    maxfla=0
    numlist = [i for i in range(len(products))]
    visit=list()
    maxcal=0
    for i in range(len(products)):
        stack.append(([i],products[i][0], products[i][1]))
        visit.append([i])
    while stack:
        menulist , flavor, cal = stack.pop()
        menulist.sort()
        if cal > L:
            continue
        else:
            if cal > maxcal:
                if maxfla > flavor:
                    continue
            if maxfla <= flavor :
                maxfla = flavor
                maxcal = cal
            for i in numlist:
                if i not in menulist:
                    newmenu = menulist+[i]
                    newmenu.sort()
                    if newmenu not in visit:
                        if cal + products[i][1] <= L :
                            stack.append((menulist+[i] , flavor + products[i][0], cal + products[i][1]))
                            visit.append(newmenu)
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