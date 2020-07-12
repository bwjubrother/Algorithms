delta = ((1, 0), (-1, 0), (0, 1), (0, -1))

T = int(input())
for i in range(T):
    n = int(input())
    board = ['1' * (n+2)]
    for _ in range(n):
        board.append('1'+str(input())+'1')
    board += ['1' * (n+2)]
    visted = [[0] * (n+2) for _ in range(n+2)]
    distance = [[0] * (n+2) for _ in range(n+2)]
    stack = []
    for x in range(n+2):
        for y in range(n+2):
            if board[x][y] == '2':
                stack = [(x, y)]
                break
        if len(stack):
            break
    ans = 0
    while stack:
        x, y = stack.pop(0)
        if not visted[x][y]:
            visted[x][y] = 1
        for j in range(4):
            newx = x + delta[j][0]
            newy = y + delta[j][1]
            if board[newx][newy] == '0' and not visted[newx][newy]:
                stack.append((newx, newy))
                distance[newx][newy] = distance[x][y] + 1
            elif board[newx][newy] == '3':
                ans = distance[x][y]
                break

    print('#%d %d' %(i+1, ans))