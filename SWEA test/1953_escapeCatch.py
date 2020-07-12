import sys
sys.stdin = open('1953.txt', 'r')

'''
# 초기코드
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def inside(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def connect(i, newx, newy):
    if i == 0:
        if board[newx][newy] == 1 or board[newx][newy] == 2 or board[newx][newy] == 4 or board[newx][newy] == 7:
            return True
    if i == 1:
        if board[newx][newy] == 1 or board[newx][newy] == 2 or board[newx][newy] == 5 or board[newx][newy] == 6:
            return True
    if i == 2:
        if board[newx][newy] == 1 or board[newx][newy] == 3 or board[newx][newy] == 6 or board[newx][newy] == 7:
            return True
    if i == 3:
        if board[newx][newy] == 1 or board[newx][newy] == 3 or board[newx][newy] == 4 or board[newx][newy] == 5:
            return True
    return False

T = int(input())
for tc in range(T):
    n, m, r, c, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    Q = [(r, c)]
    for i in range(l):
        tmp = []
        while Q:
            x, y = Q.pop(0)
            if not visited[x][y]:
                visited[x][y] = 1
            if board[x][y] == 1:
                for i in range(4):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if inside(newx, newy) and board[newx][newy] and not visited[newx][newy] and connect(i, newx, newy):
                        tmp.append((newx, newy))
            if board[x][y] == 2:
                for i in range(2):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if inside(newx, newy) and board[newx][newy] and not visited[newx][newy] and connect(i, newx, newy):
                        tmp.append((newx, newy))
            if board[x][y] == 3:
                for i in range(2, 4):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if inside(newx, newy) and board[newx][newy] and not visited[newx][newy] and connect(i, newx, newy):
                        tmp.append((newx, newy))
            if board[x][y] == 4:
                for i in range(1, 3):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if inside(newx, newy) and board[newx][newy] and not visited[newx][newy] and connect(i, newx, newy):
                        tmp.append((newx, newy))
            if board[x][y] == 5:
                for i in range(0, 4, 2):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if inside(newx, newy) and board[newx][newy] and not visited[newx][newy] and connect(i, newx, newy):
                        tmp.append((newx, newy))
            if board[x][y] == 6:
                for i in range(0, 4, 3):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if inside(newx, newy) and board[newx][newy] and not visited[newx][newy] and connect(i, newx, newy):
                        tmp.append((newx, newy))
            if board[x][y] == 7:
                for i in range(1, 4, 2):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if inside(newx, newy) and board[newx][newy] and not visited[newx][newy] and connect(i, newx, newy):
                        tmp.append((newx, newy))
        Q = tmp
    ans = 0
    for i in visited:
        ans += sum(i)
    print('#%d %d' % (tc+1, ans))
'''

#
# # 코드 다이어트
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def inside(x, y):
#     if 0 <= x < n and 0 <= y < m:
#         return True
#     return False
#
# def connect(i, newx, newy):
#     if i == 0:
#         if board[newx][newy] in (1, 2, 4, 7):
#             return True
#     if i == 1:
#         if board[newx][newy] in (1, 2, 5, 6):
#             return True
#     if i == 2:
#         if board[newx][newy] in (1, 3, 6, 7):
#             return True
#     if i == 3:
#         if board[newx][newy] in (1, 3, 4, 5):
#             return True
#     return False
#
# def find(i, x, y):
#     newx = x + dx[i]
#     newy = y + dy[i]
#     if inside(newx, newy) and board[newx][newy] and not visited[newx][newy] and connect(i, newx, newy):
#         return (newx, newy)
#     return False
#
# T = int(input())
# for tc in range(T):
#     n, m, r, c, l = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[0] * m for _ in range(n)]
#     Q = [(r, c)]
#     for i in range(l):
#         tmp = []
#         while Q:
#             x, y = Q.pop(0)
#             if not visited[x][y]:
#                 visited[x][y] = 1
#             if board[x][y] == 1:
#                 for i in range(4):
#                     if find(i, x, y):
#                         tmp.append(find(i, x, y))
#             if board[x][y] == 2:
#                 for i in range(2):
#                     if find(i, x, y):
#                         tmp.append(find(i, x, y))
#             if board[x][y] == 3:
#                 for i in range(2, 4):
#                     if find(i, x, y):
#                         tmp.append(find(i, x, y))
#             if board[x][y] == 4:
#                 for i in range(1, 3):
#                     if find(i, x, y):
#                         tmp.append(find(i, x, y))
#             if board[x][y] == 5:
#                 for i in range(0, 4, 2):
#                     if find(i, x, y):
#                         tmp.append(find(i, x, y))
#             if board[x][y] == 6:
#                 for i in range(0, 4, 3):
#                     if find(i, x, y):
#                         tmp.append(find(i, x, y))
#             if board[x][y] == 7:
#                 for i in range(1, 4, 2):
#                     if find(i, x, y):
#                         tmp.append(find(i, x, y))
#         Q = tmp
#     ans = 0
#     for i in visited:
#         ans += sum(i)
#     print('#%d %d' % (tc+1, ans))



#Teacher code
def f(N, M, R, C, L):
    q = [(R, C)]
    v = [[0]*M for _ in range(N)]
    v[R][C] = 1 # 시간
    cnt = 0
    while q:
        i, j = q.pop(0)
        cnt += 1
        if v[i][j] < L:
            for x in pipe[tunnel[i][j]]:
                ni = i + di[x]
                nj = j + dj[x]
                if 0<=ni<N and 0<=nj<M and tunnel[ni][nj]!=0 and v[ni][nj]==0 and (x+2)%4 in pipe[tunnel[ni][nj]]:
                    v[ni][nj] = v[i][j] + 1
                    q.append((ni, nj))
    return cnt

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
pipe = [[], [0,1,2,3], [1,3], [0,2], [0,3], [0,1], [1,2], [2,3],]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    r = f(N, M, R, C, L)
    print('#{} {}'.format(tc, r))
