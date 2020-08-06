import copy
from collections import deque

#dp로 풀려했는데 안됨 다익스트라로 풀어야함
'''
def solution(MAPS):
    dp=copy.deepcopy(MAPS)
    for i in range(1,len(dp[0])):
        dp[0][i]+=dp[0][i-1]
    for i in range(1,len(dp[0])):
        dp[i][0]+=dp[i-1][0]
    for i in range(1,len(dp)):
        for j in range(1,len(dp)):
            dp[i][j]=dp[i][j]+min(dp[i-1][j], dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[-1][-1]
'''
def solution(MAPS):
    visited = [[-1]*n for i in range(n)]
    checkList = deque([(0, 0)])
    visited[0][0] = MAPS[0][0]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while checkList:
        x, y = checkList.popleft()
        if x == n-1 and y == n-1:
            continue
        current_v = visited[x][y]
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            # 범위 초과
            if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n:
                continue
            # 첫 비용 계산이거나, 기록된 비용보다 최소 비용일
            if visited[temp_x][temp_y] == -1 or \
                current_v + MAPS[temp_x][temp_y] < visited[temp_x][temp_y]:
                visited[temp_x][temp_y] = current_v + MAPS[temp_x][temp_y]
                checkList.append((temp_x, temp_y))

    return visited[n-1][n-1]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    MAPS=[list(map(int,list(input()))) for _ in range(n)]
    print("#"+str(test_case),solution(MAPS))
