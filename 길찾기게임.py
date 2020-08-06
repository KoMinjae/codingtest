from sys import setrecursionlimit 
setrecursionlimit(10000000)
class Tree():
        def __init__(self, number,data):
            self.number = number
            self.data = data
            self.left = None
            self.right = None

preorderlist=[]
postoderlist=[]

def solution(nodeinfo):
    nodedict = [node for node in nodeinfo]
    Trees=[]
    answer = []
    nodeinfo.sort(key= lambda x:(-x[1],x[0]))
    root = None
    for node in nodeinfo:
        if not root:
            root = Tree(nodedict.index(node),node)
        else:
            current = root
            while True:
                if node[0]<current.data[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(nodedict.index(node),node)
                        break
                elif node[0] > current.data[0]:
                    if current.right:
                        current=current.right
                        continue
                    else:
                        current.right = Tree(nodedict.index(node),node)
                        break
                break
    preorder(root)
    postorder(root)
    answer.append(preorderlist)
    answer.append(postoderlist)
    return answer
def preorder(node):
    preorderlist.append(node.number+1)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    postoderlist.append(node.number+1)
solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])