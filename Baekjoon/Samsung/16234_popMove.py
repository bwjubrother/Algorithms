import sys
sys.stdin = open('16234.txt', 'r')


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 좌 우 상 하
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

# n^2
cnt = 0
while True:
    _board = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                q = [(x, y)]
                lands = [(x, y)]
                sum_pop = board[x][y]
                while q:
                    x, y = q.pop(0)
                    for i in range(4):
                        nx = x+dx[i]
                        ny = y+dy[i]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(board[x][y] - board[nx][ny]) <= r:
                            q.append((nx, ny))
                            lands.append((nx, ny))
                            sum_pop += board[nx][ny]
                            visited[nx][ny] = True
                lands = list(set(lands))
                if len(lands) >= 2:
                    for x, y in lands:
                        _board[x][y] = sum_pop // len(lands)
    sum_row = 0
    for row in _board:
        sum_row += sum(row)
    if sum_row == 0:
        break
    cnt += 1
    for x in range(n):
        for y in range(n):
            if _board[x][y]:
                board[x][y] = _board[x][y]
    print(board)

print(cnt)