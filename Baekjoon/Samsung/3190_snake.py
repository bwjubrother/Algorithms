import sys
sys.stdin = open('3190.txt', 'r')


n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
# 사과의 위치 = 1
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
l = int(input())
rotate = [list(input().split()) for _ in range(l)]
t = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 뱀 몸의 위치 = 2
board[0][0] = 2
# snake 머리 sx, sy
sx, sy = 0, 0
snake = [(0, 0)]
dirs_idx = 0
crash = 0
for rot in rotate:
    while t < int(rot[0]):
        t += 1
        nx = sx + dirs[dirs_idx][0]
        ny = sy + dirs[dirs_idx][1]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
            if not board[nx][ny]:
                tx, ty = snake.pop(0)
                board[tx][ty] = 0
            board[nx][ny] = 2
            snake.append((nx, ny))
            sx = nx
            sy = ny
        else:
            crash = 1
            break
    if crash:
        break
    if rot[1] == 'D':
        dirs_idx = (dirs_idx + 1) %  4
    elif rot[1] == 'L':
        dirs_idx = (dirs_idx - 1) %  4

if not crash:
    while True:
        t += 1
        nx = sx + dirs[dirs_idx][0]
        ny = sy + dirs[dirs_idx][1]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
            if not board[nx][ny]:
                tx, ty = snake.pop(0)
                board[tx][ty] = 0
            board[nx][ny] = 2
            snake.append((nx, ny))
            sx = nx
            sy = ny
        else:
            break
print(t)