class Tree:
    def __init__(self, N):
        self.lst = [0] * (N + 1)
        self.N = N

    def put(self, num1, num2):  # leaf 입력
        self.lst[num1] = num2

    def search_leaf(self, node):
        if node * 2 > N:  # leaf
            self.sum += self.lst[node]  # 누적 합
        else:  # branch
            self.search_leaf(node * 2)  # left 탐색
            if node * 2 != N:  # right 존재하면
                self.search_leaf(node * 2 + 1)  # right 탐색

    # 노드L의 자식들 중 leaf만 찾아 누적 합 리턴
    def my_result(self, L):
        self.sum = 0
        self.search_leaf(L)
        return self.sum


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = Tree(N)
    for _ in range(M):
        num1, num2 = map(int, input().split())
        tree.put(num1, num2)
    print('#{} {}'.format(test_case, tree.my_result(L)))