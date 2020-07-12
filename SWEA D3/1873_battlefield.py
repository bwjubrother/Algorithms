import sys
sys.stdin = open('1873.txt', 'r')


def inside(x, y):
    if 0 <= x < h and 0 <= y < w:
        return True
    return False

def act(l):
    global tank, xt, yt
    if l == 'S':
        if tank == '<':
            for y in range(yt-1, -1, -1):
                if board[xt][y] == '#':
                    break
                if board[xt][y] == '*':
                    board[xt][y] = '.'
                    break
        if tank == '>':
            for y in range(yt+1, w):
                if board[xt][y] == '#':
                    break
                if board[xt][y] == '*':
                    board[xt][y] = '.'
                    break
        if tank == '^':
            for x in range(xt-1, -1, -1):
                if board[x][yt] == '#':
                    break
                if board[x][yt] == '*':
                    board[x][yt] = '.'
                    break
        if tank == 'v':
            for x in range(xt+1, h):
                if board[x][yt] == '#':
                    break
                if board[x][yt] == '*':
                    board[x][yt] = '.'
                    break
    if l == 'U':
        nx = xt-1
        if inside(nx, yt) and board[nx][yt] == '.':
            board[nx][yt] = '^'
            board[xt][yt] = '.'
            xt = nx
            tank = '^'
        else:
            board[xt][yt] = '^'
            tank = '^'
    if l == 'D':
        nx = xt+1
        if inside(nx, yt) and board[nx][yt] == '.':
            board[nx][yt] = 'v'
            board[xt][yt] = '.'
            xt = nx
            tank = 'v'
        else:
            board[xt][yt] = 'v'
            tank = 'v'
    if l == 'L':
        ny = yt-1
        if inside(xt, ny) and board[xt][ny] == '.':
            board[xt][ny] = '<'
            board[xt][yt] = '.'
            yt = ny
            tank = '<'
        else:
            board[xt][yt] = '<'
            tank = '<'
    if l == 'R':
        ny = yt+1
        if inside(xt, ny) and board[xt][ny] == '.':
            board[xt][ny] = '>'
            board[xt][yt] = '.'
            yt = ny
            tank = '>'
        else:
            board[xt][yt] = '>'
            tank = '>'

T = int(input())
for tc in range(T):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    n = int(input())
    ip = input()
    for xs in range(h):
        for ys in range(w):
            if board[xs][ys] == '<' or board[xs][ys] == '^' or board[xs][ys] == 'v' or board[xs][ys] == '>':
                xt, yt = xs, ys
                tank = board[xs][ys]
                break
    for i in ip:
        act(i)

    print('#%d' % (tc+1), end=' ')
    for row in board:
        print(''.join(row))


