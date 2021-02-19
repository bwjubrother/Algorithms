import sys
sys.stdin = open('1976.txt', 'r')


'''
# 일일히 찾기
def travel(start, end, board):
    stack = [start]
    while stack:
        for item in stack:
            for idx, dest in enumerate(board[item]):
                if dest == 1:
                    if idx == end:
                        return True
                    else:
                        stack.append(idx)
    return False
                    
N = int(input())
M = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))
plan = list(map(int, input().split(' ')))
start = plan[0]
for dest in plan[1:]:
    if not travel(start-1, dest-1, board):
        print('NO')
        quit()
    else:
        start = dest
print('YES')
'''

def find(i, rst):
    if rst[i] != i:
        rst[i] = find(rst[i], rst)
    return rst[i]

def union(i, j, rst):
    x = find(i, rst)
    y = find(j, rst)
    rst[x] = y

# union-find
N = int(input())
M = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))
plan = [int(x) - 1 for x in input().split(' ')]
rst = list(range(N))
for i in range(N):
    for j in range(i+1, N):
        if board[i][j] == 1:
            union(i, j, rst)
pivot = find(plan[0], rst)
for i in range(1, M):
    if pivot != find(plan[i], rst):
        print('NO')
        quit()
print('YES')