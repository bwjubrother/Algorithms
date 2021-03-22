import sys
sys.stdin = open('15685.txt', 'r')

# 우 상 좌 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(n):
    y, x, d, g = map(int, input().split())
    board[x][y] = 1
    x += dx[d]
    y += dy[d]
    board[x][y] = 1
    dragon = [d]
    for _ in range(g):
        for nd in dragon[::-1]:
            _d = (nd+1) % 4
            x += dx[_d]
            y += dy[_d]
            board[x][y] = 1
            dragon.append(_d)

# 사각형 찾기
cnt = 0
for x in range(100):
    for y in range(100):
        if board[x][y] == 1:
            if board[x][y+1] == 1 and board[x+1][y] == 1 and board[x+1][y+1] == 1:
                cnt += 1
print(cnt)


