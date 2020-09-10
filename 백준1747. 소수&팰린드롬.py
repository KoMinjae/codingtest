Eratos = [0]*1000001
Eratos[0] = 0
Eratos[1] = 1
for i in range(2,1000):
    if Eratos[i]==0:
        temp = i+i
        while temp<1000000:
            Eratos[temp]=1
            temp=temp+i

def solution(N):
    for i in range(N,1000001):
        if Eratos[i] == 0:
            if list(str(i)) == list(str(i)[::-1]):
                return i
    #N이 10000000을 넘는 결과값일 때 가장 작은 소수&팰린드롬
    return 1003001
def main():
    N = int(input())
    print(solution(N))

main()