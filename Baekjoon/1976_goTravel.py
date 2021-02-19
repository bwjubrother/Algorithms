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

# union-find
N = int(input())
M = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))
plan = list(map(int, input().split(' ')))
rst = list(range(N))
print(rst)