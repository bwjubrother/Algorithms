import sys
sys.stdin = open('13460.txt', 'r')


# 다음이 벽이거나 현재가 구멍일 때 까지 dx, dy 더함
def move(x, y, dx, dy):
    dist = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        dist += 1
    return x, y, dist


# bfs 탐색, 나오면 종료
def bfs(rx, ry, bx, by):
    # 좌, 우, 상, 하
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    q = [(rx, ry, bx, by, 0)]
    visited = []
    while q:
        rx, ry, bx, by, cnt = q.pop(0)
        if cnt > 10:
            break
        for i in range(4):
            _rx, _ry, rdist = move(rx, ry, dx[i], dy[i])
            _bx, _by, bdist = move(bx, by, dx[i], dy[i])
            if board[_bx][_by] == 'O':
                continue
            else:
                if board[_rx][_ry] == 'O':
                    print(cnt+1)
                    return
                if (_rx, _ry) == (_bx, _by):
                    if rdist > bdist:
                        _rx -= dx[i]
                        _ry -= dy[i]
                    else:
                        _bx -= dx[i]
                        _by -= dy[i]
                if not (_rx, _ry, _bx, _by) in visited:
                    visited.append((_rx, _ry, _bx, _by))
                    q.append((_rx, _ry, _bx, _by, cnt+1))
    print(-1)
    return

n, m = map(int, input().split())
# 좌 (0, -1) 우 (0, 1) 위 (-1, 0) 아래(1, 0)
board = [list(input()) for _ in range(n)]

# 현재 공의 위치 찾기
for x in range(n):
    for y in range(m):
        if board[x][y] == 'R':
            rx, ry = x, y
        elif board[x][y] == 'B':
            bx, by = x, y

bfs(rx, ry, bx, by)