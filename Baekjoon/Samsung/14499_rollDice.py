import sys
sys.stdin = open('14499.txt', 'r')


n, m, r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rolls = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0]
dirs = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]
x, y = r, c
for roll in rolls:
    nx, ny = x+dirs[roll][0], y+dirs[roll][1]
    if 0 <= nx < n and 0 <= ny < m:
        if roll == 1:
            dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
        elif roll == 2:
            dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
        elif roll == 3:
            dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]   
        elif roll == 4:
            dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
        if board[nx][ny]:
            dice[6] = board[nx][ny]
            board[nx][ny] = 0
        else:
            board[nx][ny] = dice[6]
        x, y = nx, ny
        print(dice[1])
