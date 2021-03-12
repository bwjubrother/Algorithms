import sys
sys.stdin = open('15683.txt', 'r')


from copy import deepcopy


def count(board):
    zero = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                zero += 1
    # for i in board:
    #     print(i)
    return zero


def fill(x, y, dirs, board):
    _board = deepcopy(board)
    for d in dirs:
        _x = x+dx[d]
        _y = y+dy[d]
        q = [(_x, _y)]
        while q:
            nx, ny = q.pop(0)
            if 0 <= nx < n and 0 <= ny < m:
                if _board[nx][ny] == 6:
                    break
                elif _board[nx][ny] == 0:
                    _board[nx][ny] = -1
                    q.append((nx+dx[d], ny+dy[d]))
                elif _board[nx][ny] == -1:
                    q.append((nx+dx[d], ny+dy[d]))
    return _board


def dfs(idx, board):
    global min_zero
    if idx == len(cctv):
        min_zero = min(min_zero, count(board))
        return
    x, y, num = cctv[idx]
    for dirs in cover[num]:
        _board = fill(x, y, dirs, board)
        dfs(idx+1, _board)

n, m = map(int, input().split())
# 1번은 한쪽, 2번은 양쪽, 3번은 ㄱ자, 4번은 3방향, 5번은 4방향, 6번 벽
# 사각지대의 최소 크기 = 최소 0의 갯수
board = [list(map(int, input().split())) for _ in range(n)]
# cctv 찾기
cctv = []
for x in range(n):
    for y in range(m):
        if board[x][y] in (1, 2, 3, 4, 5):
            cctv.append((x, y, board[x][y]))
# 좌 우 상 하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] 
cover = [[], [[0], [1], [2], [3]],[[0, 1], [2, 3]], 
    [[0, 2], [2, 1], [1, 3], [3, 0]], [[0, 1, 2],[1, 2, 3],[2, 3, 0], [0, 1, 3]], [[0, 1, 2, 3]]]

min_zero = n * m
dfs(0, board)
print(min_zero)

'''
정답 풀이
from copy import deepcopy
import sys
input = sys.stdin.readline
def fill(x, y, arr, d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 6:
                    break
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = "#"
            else:
                break
def dfs(arr, cnt):
    global result
    temp = deepcopy(arr)
    if cnt == cctv_cnt:
        num = 0
        for i in range(n):
            num += temp[i].count(0)
        result = min(result, num)
        return
    x, y, cctv = q[cnt]
    for i in direction[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt + 1)
        temp = deepcopy(arr)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]], 
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
n, m = map(int, input().split())
s = []
q = []
cctv_cnt = 0
result = 100000000
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(len(a)):
        if a[j] != 0 and a[j] != 6:
            q.append([i, j, a[j]])
            cctv_cnt += 1
dfs(s, 0)
print(result)
'''