import sys
sys.stdin = open('17472.txt', 'r')


import math
from collections import deque, defaultdict

# 섬 구분하기
def bfs(start, board, land_num):
    q = [start]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        x, y = q.pop()
        board[x][y] = land_num
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[nx][ny] = land_num
                q.append((nx, ny))
    return


def get_distance(board):
    table = defaultdict(lambda: math.inf)

    # 가로, 세로
    iters = [board, list(map(list, zip(*board)))]
    for _board in iters:
        for x in range(len(_board)):
            land = None
            checked = set()
            for y in range(1, len(_board[0])):
                if _board[x][y] == 0 and _board[x][y-1] != 0:
                    land = y-1
                if _board[x][y] != 0 and land is not None:
                    distance = y - land - 1
                    if distance >= 2 and _board[x][y] not in checked:
                        small = min(_board[x][land], _board[x][y])
                        large = max(_board[x][land], _board[x][y])
                        table[(small, large)] = min(table[(small, large)], distance)
                    checked.add(_board[x][y])
    return table


def get_parent(x, parent):
    if x == parent[x]:
        return x
    p = get_parent(parent[x], parent)
    parent[x] = p
    return p


def union_find(x, y, parent):
    x = get_parent(x, parent)
    y = get_parent(y, parent)
    parent[x] = y


def get_min_distance(table, lands):
    table = sorted(list(table.items()), key = lambda x:x[1])
    result = 0

    # union-find
    parent = {i:i for i in range(2, max(lands)+1)}
    
    for (x, y), value in table:
        if get_parent(x, parent) != get_parent(y, parent):
            union_find(x, y, parent)
            result += value
        
        if len(set([get_parent(i, parent) for i in parent])) == 1:
            return result
    return -1


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 다리의 갯수는 섬 갯수 - 1
# 섬의 위치 찾기
land_num = 2
for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            bfs((x, y), board, land_num)
            land_num += 1

# 각 섬마다 거리를 계산 (길이 2이상)
table = get_distance(board)

# 가장 긴 거 빼고 선택
print(get_min_distance(table, set(range(2, land_num))))