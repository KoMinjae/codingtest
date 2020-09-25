def main():
    N = int(input())
    graph = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(int(input())):
        a,b = map(int,input().split())
        graph[a-1][b-1]=1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j]=1
    for i in range(N):
        ans = 0
        for j in range(N):
            if not graph[i][j] and not graph[j][i]:
                ans += 1
        print(ans-1)

main()