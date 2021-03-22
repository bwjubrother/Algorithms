t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1

    ans = 0
    visited = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for x in range(n):
        for y in range(m):
            if board[x][y] and (x, y) not in visited:
                visited.append((x, y))
                q = [(x, y)]
                while q:
                    _x, _y = q.pop()
                    for i in range(4):
                        nx = _x+dx[i]
                        ny = _y+dy[i]
                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and (nx, ny) not in visited:
                            visited.append((nx, ny))
                            q.append((nx, ny))  
                ans += 1
    print(ans)
