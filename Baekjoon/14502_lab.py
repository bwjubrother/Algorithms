# import sys
from copy import deepcopy
# sys.stdin = open('14502.txt', 'r')


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 바이러스 퍼지기
def virusSpread(x, y, copied):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not copied[nx][ny]:
            copied[nx][ny] = 2
            virusSpread(nx, ny, copied)

# 안전구역 넓이 구하기
def cntSafe(copied):
    cnt = 0
    for x in range(n):
        for y in range(m):
            if not copied[x][y]:
                cnt += 1
    return cnt

# 무작위로 벽 3개 세우기
def makeWall(start, avail):
    global maxcnt
    if avail == 3:
        copied = deepcopy(board)
        leng = len(virusList)
        for i in range(leng):
            X, Y = virusList[i]
            virusSpread(X, Y, copied)
        maxcnt = max(maxcnt, cntSafe(copied))
        return
    for i in range(start, n*m):
        x = int(i / m)
        y = int(i % m)

        if not board[x][y]:
            board[x][y] = 1
            makeWall(i+1, avail+1)
            board[x][y] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virusList = []
for x in range(n):
    for y in range(m):
       if board[x][y] == 2:
           virusList.append((x, y))
maxcnt = 0
makeWall(0, 0)
print(maxcnt)