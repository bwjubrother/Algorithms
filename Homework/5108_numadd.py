import sys

sys.stdin = open('5108.txt', 'r')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class linkedList:
    def __init__(self, data):
        new_node = None(data)
        self.head = new_node
        self.list_size = 1

    def __str__(self):
        print_list = ''
        node = self.head
        while True:
            print_list += str(node)
            if node.next == None:
                break
            node = node.next
            print_list += ', '
        return print_list

    def insertFirst(self, data):
        new_node = Node(data)
        tmp = self.head
        self.head = new_node
        self.head.next = tmp
        self.list_size += 1

    def insertMiddle(self, num, data):
        if self.head.next == None:
            insertLast(data)
            return
        node = self.selectNode(num)
        new_node = Node(data)
        tmp = node.next
        node.next = new_node
        new_node.next = tmp
        self.list_size += 1

    def insertLast(self, data):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next

        new_node = Node(data)
        node.next = new_node
        self.list_size += 1

    def selectNode(self, num):
        if self.list_size < num:
            print('Overflow')
            return
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node

    def delectNode(self, num):
        if num == 0:
            node = self.head
            self.head = node.next
            del node
        else:
            node = self.selectNode(num-1)
            node.next = node.next.next
            del_node = node.next
            del del_node


T = int(input())

for i in range(T):
    n, m, l = map(int, input().split())
    numlist = input().split()
    for j in range(m):
        ans = []
        idx, num = map(int, input().split())
        ans += numlist[:idx]
        ans.append(str(num))
        ans += numlist[idx:]
        numlist = ans
    print('#%d %s' % (i+1, ans[l]))
