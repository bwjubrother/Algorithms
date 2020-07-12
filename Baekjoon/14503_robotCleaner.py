import sys
sys.stdin = open('14503.txt', 'r')


dx = [-1, 0, 1, 0] #북, 동, 남, 서
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 1
board[r][c] = 2
while True:
    nd = d
    for _ in range(4):
        go = 0
        nd -= 1
        if nd == -1:
            nd = 3
        nx = r + dx[nd]
        ny = c + dy[nd]
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            r, c = nx, ny
            d = nd
            ans += 1
            go = 1
            break
    if not go:  #4방향이 다 1이거나 2이면 후진
        if d == 0:
            r += 1
        elif d == 1:
            c -= 1
        elif d == 2:
            r -= 1
        elif d == 3:
            c += 1
        if board[r][c] == 1: # 후진했는데 벽이면 break
            break
print(ans)