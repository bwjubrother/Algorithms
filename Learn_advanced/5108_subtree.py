class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self, cnt):
        self.node_lst = [None]
        for i in range(E + 1):
            self.node_lst.append(Node(i))

    def put(self, parent, child):
        if self.node_lst[parent].left == None:
            self.node_lst[parent].left = self.node_lst[child]
        else:
            self.node_lst[parent].right = self.node_lst[child]

    def count(self, node):
        self.cnt += 1
        if node.left != None:
            self.count(node.left)
        if node.right != None:
            self.count(node.right)

    def my_result(self, num):
        self.cnt = 0
        self.count(self.node_lst[num])
        return self.cnt


T = int(input())
for test_case in range(1, 1 + T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = Tree(E)
    for i in range(E):
        tree.put(data[2 * i], data[2 * i + 1])
    print('#{} {}'.format(test_case, tree.my_result(N)))