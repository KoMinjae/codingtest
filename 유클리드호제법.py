def UC(X, Y):
    while(Y):
        X, Y = Y, X%Y
    return X

#유클리드 호제법을 이용한 최소공배수 구하기
def UC2(X, Y):
    result = (X*Y) // UC(X,Y)
    return result

N,M = map(int,input().split())
N,M = max(N,M), min(N,M)
print(UC(N,M), UC2(N,M))
