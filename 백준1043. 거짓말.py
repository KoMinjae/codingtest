N, M = map(int,input().split())
trueman = list(map(int,input().split()))
trueman.pop(0)
truemanlist = set(trueman)
party=list()
for i in range(M):
    line = list(map(int,input().split()))[1:]
    if not truemanlist.isdisjoint(set(line)):
        truemanlist = truemanlist.union(set(line))
    party.append(line)
for i in range(M):
    for j in range(M):
        if not truemanlist.isdisjoint(set(party[j])):
            truemanlist = truemanlist.union(set(party[j]))
count = 0
for i in party:
    if truemanlist.isdisjoint(set(i)):
        count+=1
print(count)
