import sys
from collections import deque
input = sys.stdin.readline
"""def solution(graph,questions):
    answer = list()
    notanswer = list()
    answers=[0]*len(questions)
    for idx, question in enumerate(questions):
        a, b = question
        queue = deque()
        visitied = set()
        queue.append(a)
        visitied.add(a)
        while queue:
            node = queue.popleft()
            if node == b:
                answer.append(idx)
                break
            else:
                for i in graph[node]:
                    if i not in visitied:
                        queue.append(i)
                        visitied.add(i)
    
    for idx, question in enumerate(questions):
        b, a = question
        queue = deque()
        visitied = set()
        queue.append(a)
        visitied.add(a)
        while queue:
            node = queue.popleft()
            if node == b:
                notanswer.append(idx)
                break
            else:
                for i in graph[node]:
                    if i not in visitied:
                        queue.append(i)
                        visitied.add(i)

    for i in range(len(questions)):
        if i in answer:
            answers[i] = -1
        elif i in notanswer:
            answers[i] = 1
        else:
            answers[i] = 0
    return answers"""
############dfs, bfs로 풀면 시간초과 플로이드마샬로 풀어야함#############
def main():
    N, M = map(int,input().split())
    #graph = dict()
    maps = [[0 for _ in range(N)]for _ in range(N)]
    
    #for i in range(N):
        #graph.setdefault(i,list())

    for i in range(M):
        first, late = map(int,input().split())
        maps[first-1][late-1]=1
        #graph[first-1].append(late-1)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if maps[i][k] and maps[k][j]:
                    maps[i][j] = 1
    questions = list()
    for _ in range(int(input())):
        a, b= map(int,input().split())
        questions.append((a-1,b-1))
    #answer = solution(graph,questions)
    for i in questions:
        a,b = i[0],i[1]
        if maps[a][b] == 1:
            print(-1)
        elif maps[b][a] == 1:
            print(1)
        else:
            print(0)

main()

