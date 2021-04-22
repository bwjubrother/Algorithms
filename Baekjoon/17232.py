import sys
sys.stdin = open('17232.txt', 'r')

n, m, t = map(int, input().split())
k, a, b = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

time = 0
while time < t:
    time += 1
    _board = [['.' for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            around = 0
            for dx in range(-k, k+1):
                for dy in range(-k, k+1):
                    if dx == dy == 0:
                        continue
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == '*':
                        around += 1
            if board[x][y] == '*':
                if a <= around <= b:
                    _board[x][y] = '*'
                else:
                    _board[x][y] = '.'
            else:
                if a < around <= b:
                    _board[x][y] = '*'
    board = _board

for row in board:
    print(''.join(row))