import sys

sys.stdin = open('9640.txt', 'r')


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())

for i in range(T):
    seq = list(map(int, input().split()))
    m = int(input())
    board = [list(map(int, input().split())) for _ in range(m)]
    stack = []
    visited = [[0] * m for _ in range(m)]
    ans = 0
    for x in range(m):
        for y in range(m):
            if board[x][y] == seq[1]:
                stack.append((x, y))
    go = 0
    for num in seq[2:]:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = 1
        for k in range(4):
            newx = x + delta[k][0]
            newy = y + delta[k][1]
            if 0<=newx<m and 0<=newy<m and not visited[newx][newy] and board[newx][newy] == num:
                stack.append((newx, newy))
                go += 1
                if go == seq[0] - 1:
                    ans = 1
                    break
    print('#%d %d' %(i+1, ans))