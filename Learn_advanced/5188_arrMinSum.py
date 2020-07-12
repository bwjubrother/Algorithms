import sys
sys.stdin = open('5188.txt', 'r')


dx = [1, 0]
dy = [0, 1]

def go(x, y, s):
    global mins
    if mins != float('inf') and s > mins:
        return
    if x == n-1 and y == n-1:
        if s < mins:
            mins = s
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < n and ny < n:
                go(nx, ny, s+board[nx][ny])

T = int(input())
for tc in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    mins = float('inf')
    go(0, 0, board[0][0])
    print('#%d %d' % (tc+1, mins))