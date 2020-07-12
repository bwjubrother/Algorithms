import sys

sys.stdin = open('16236.txt', 'r')

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def findRoad(size):
    newboard = []
    newboard.append([7] * (n+2))
    for i in range(n):
        newboard.append([7] + board[i] + [7])
    newboard.append([7] * (n+2))
    for x in range(n+2):
        for y in range(n+2):
            if newboard[x][y] >= size:
                newboard[x][y] = 7


for x in range(n):
    for y in range(n):
        if board[x][y] == 9:
            xs, ys = x, y
            break

findRoad(2)
