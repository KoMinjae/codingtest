def solution(paths):
    stack=list()
    stack.append(('0',['0']))
    visited=list()
    while stack:
        node, path = stack.pop()
        if node == '99':
            return 1
        if node not in visited:
            visited.append(node)
            if node in paths:
                for m in paths[node]:
                    stack.append((m,path+[m]))
    return 0
def gen():
    table = dict()
    t, e = map(int, input().strip().split())
 
    start = None
    for v in map(int, input().strip().split()):
        if start is None:
            start = v
        else:
            if str(start) in table:
                table[str(start)].append(str(v))
            else:
                table[str(start)] = [str(v)]
            start = None
    yield t, table
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(10):
        for t, table in gen():
            print("#{0} {1}".format(t, solution(table)))