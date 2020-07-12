import sys
sys.stdin = open('5250.txt', 'r')


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    key = [[float('inf')] * N for _ in range(N)]
    key[0][0] = 0
    stack = {(0, 0)}

    while True:
        min_key = float('inf')
        for r, c in stack:
            if key[r][c] < min_key and not visited[r][c]:
                min_key = key[r][c]
                x, y = r, c

        if x == y == N-1:
            ans = key[x][y]
            break

        visited[x][y] = True
        stack.remove((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[x][y] < board[nx][ny]:
                    fuel = key[x][y] + (board[nx][ny] - board[x][y]) + 1
                else:
                    fuel = key[x][y] + 1
                if fuel < key[nx][ny]:
                    key[nx][ny] = fuel
                    stack.add((nx, ny))

    print('#%d %d' %(tc+1, ans))