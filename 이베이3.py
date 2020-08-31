def solution(n, products):
    answer = 0
    maxs=0
    maxidx=list()
    maedae=None
    products.sort(key=lambda x:-(x[1]*x[2]))
    while n!=0:
        popidx=list()
        maxs=0
        for i in range(len(products)):
            if products[i][0] >= products[i][2]*n:
                if products[i][0] >= products[i][2]*2:
                    price = products[i][1]*products[i][2]*2
                else:
                    price = products[i][0]*products[i][1]
                if maxs<price:
                    maxs=price
                    maedae = i
        if maedae==None:
            maedae=0
        for i in range(len(products)):
            if i == maedae:
                if products[i][0]>=products[i][2]*2:
                    answer+=products[i][1]*products[i][2]*2
                    products[i][0]=products[i][0]-products[i][2]*2
                else:
                    answer+=products[i][0]*products[i][1]
                    products[i][0]=products[i][0]-products[i][2]*2
            else:
                if products[i][0]>=products[i][2]:
                    answer+=products[i][1]*products[i][2]
                    products[i][0]=products[i][0]-products[i][2]
                else:
                    answer+=products[i][0]*products[i][1]
                    products[i][0]=products[i][0]-products[i][2]
        for i in range(len(products)):
            if products[i][0] <=0:
                popidx.append(i)
        for i in popidx:
            products.pop(i)

        n-=1
    
    
    return answer


solution(3, [[6, 5, 1], [11, 3, 2], [7, 10, 3]])