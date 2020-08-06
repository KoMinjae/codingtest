'''
from collections import deque as queue

transistable = lambda a,b: sum((1 if x!=y else 0) for x,y in zip(a,b)) == 1

def solution(begin,target,words):
    q, d = queue(), dict()
    q.append((begin, 0))
    d[begin] = set(filter(lambda x:transistable(x,begin), words))
    
    for w in words:
        d[w] = set(filter(lambda x:transistable(x,w), words))
       
    while q:
        cur, level  = q.popleft()
        if level > len(words):
            return 0
        for w in d[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))
    
    return 0
'''

def solution(begin,target,words):
    answer = 0
    if target not in words:
        return 0
    stack = list()
    stack.append(begin)
    visited=list()
    visited.append(begin)
    while stack:
        word = stack.pop()
        if word == target:
            return answer
        else:
            for i in range(len(words)):
                if len([j for j in range(len(words[i])) if words[i][j]!=word[j]])==1:
                    if words[i] not in visited:
                        visited.append(words[i])
                        stack.append(words[i])
        answer+=1
    return answer
solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])