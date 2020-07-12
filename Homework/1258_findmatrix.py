import sys

sys.stdin = open('1258.txt', 'r')

def findcol(x, y):
    col = 0
    for yy in range(y, n):
        if board[x - 1][yy]:
            col += 1
        else:
            return col

T = int(input())
for i in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    results = []
    row, y = 0, 0
    while y < n:
        cols = []
        for x in range(n):
            tmp = []
            if board[x][y]:
                row += 1
            elif row:
                tmp.append(row)
                tmp.append(findcol(x, y))
                tmp = [tmp[0] * tmp[1]] + tmp
                results.append(tmp)
                cols.append(tmp[2])
                row = 0
        if row:
            tmp.append(row)
            tmp.append(findcol(x, y))
            tmp = [tmp[0] * tmp[1]] + tmp
            results.append(tmp)
            cols.append(tmp[2])
        if cols:
            y += max(cols)
        else:
            y += 1
    ans = sorted(results)
    anslist = []
    for j in ans:
        anslist.append(str(j[1]))
        anslist.append(str(j[2]))
    print('#%d %d %s' % (i+1, len(ans), ' '.join(anslist)))