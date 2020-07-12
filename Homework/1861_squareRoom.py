import sys
sys.stdin = open('1861.txt', 'r')


delta = ((1, 0 ), (-1, 0), (0, 1), (0, -1))

def inBoard(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

T = int(input())
for tc in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    distance = [[1] * n for _ in range(n)]
    maxd = 0
    for x in range(n):
        for y in range(n):
            newx = x
            newy = y
            while True:
                for i in range(4):
                    if inBoard(newx+delta[i][0], newy+delta[i][1]) and board[newx+delta[i][0]][newy+delta[i][1]] == board[newx][newy] + 1:
                        distance[x][y] += 1
                        newx += delta[i][0]
                        newy += delta[i][1]
                        break
                else:
                    break
            if maxd < distance[x][y]:
                maxd = distance[x][y]
    minx = float('inf')
    for x in range(n):
        for y in range(n):
            if distance[x][y] == maxd and board[x][y] < minx:
                minx = board[x][y]
    print('#%d %d %d' % (tc+1, minx, maxd))
