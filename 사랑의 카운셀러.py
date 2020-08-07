from itertools import combinations as comb

def solve():
    global ans, N
    a = sum_of_list(worm)
    for minus in comb(worm, N // 2):
        temp = [0,0]
        b = sum_of_list(minus)
        temp[0] = a[0] - b[0] * 2
        temp[1] = a[1] - b[1] * 2
        temp = temp[0] ** 2 + temp[1] ** 2
        ans = min(temp,ans)

def sum_of_list(list_):
    res = [0, 0]
    for each in (list_):
        res[0] += each[0]
        res[1] += each[1]
    return res
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ans = 10000000000000000
    worm = []
    for i in range(N):
        worm.append(list(map(int, input().split())))
    solve()
    print(f'#{tc} {ans}')