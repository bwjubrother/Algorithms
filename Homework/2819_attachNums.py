import sys
sys.stdin = open('2819.txt', 'r')


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

def find(x, y, n, s):
    if (n == 7):
        cases.add(s)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < 4 and 0 <= ny < 4):
                find(nx, ny, n + 1, s + board[x][y])

for tc in range(T):
    board = [list(input().split()) for i in range(4)]
    cases = set()
    for x in range(4):
        for y in range(4):
            find(x, y, 0, '')
    print('#%d %d' % (tc+1, len(cases)))