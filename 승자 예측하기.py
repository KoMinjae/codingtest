'''class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def depth(self):
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1
class Tree:
    def __init__(self):
        self.root = None
    def depth(self):
        if self.root: return self.root.depth()
        else: return 0
    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    X=1
    count=0
    '''node=list()
    tree=Tree()
    node.append(Node(1))
    for i in range(1,(N//2)+1):
        if 2*i <= N:
            node.append(Node(2*i))
        if 2*i+1<=N:
            node.append(Node((2*i)+1))
    for i in range(int(len(node)/2)):
        tree.makeRoot(node[i],node[i*2+1],node[i*2+2])
    print(tree.depth())'''
    if N == 1:
        answer="Bob"
        print('#{} {}'.format(test_case, answer))

    else:
        while True:
            if 2**count<= N <= 2**(count+1)-1 :
                if count % 2 == 0:
                    if N==2**count:
                        answer="Alice"
                    else : 
                        answer = "Bob"
                else : 
                    if N==2**count:
                        answer="Bob"
                    else : 
                        answer = "Alice"
                print('#{} {}'.format(test_case, answer))
                break
            count+=1
