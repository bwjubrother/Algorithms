import sys

sys.stdin = open('test.txt', 'r')

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())

for i in range(T):
    n = int(input())
    board = [[1] * (n+2)]
    for _ in range(n):
        board.append([1]+list(map(int, list(input())))+[1])
    board.append([1] * (n+2))

    xs, ys = 0, 0
    for x in range(n+2):
        for y in range(n+2):
            if board[x][y] == 2:
                xs = x
                ys = y
                break
        if xs != 0:
            break

    stack = [(xs, ys)]
    visited = [[0] * (n+2) for _ in range(n+2)]
    result = []
    while stack:
        x = stack.pop()[0]
        y = stack.pop()[1]
        if not visited[x][y]:
            visited[x][y] = 1

        for j in range(4):
            if not visited[x+delta[j][0]][y+delta[j][1]] and not board[x+delta[j][0]][y+delta[j][1]]:
                stack.append((x+delta[j][0], y+delta[j][1]))
            if board[x+delta[j][0]][y+delta[j][1]] == 3:
                break
