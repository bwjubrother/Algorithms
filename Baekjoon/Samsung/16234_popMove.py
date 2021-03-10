import sys
sys.stdin = open('16234.txt', 'r')


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 좌 우 상 하
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

# n^2
cnt = 0
while True:
    _board = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                q = [(x, y)]
                lands = [(x, y)]
                sum_pop = 0
                while q:
                    x, y = q.pop(0)
                    for i in range(4):
                        nx = x+dx[i]
                        ny = y+dy[i]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(board[x][y] - board[nx][ny]) <= r:
                            q.append((nx, ny))
                            lands.append((nx, ny))
                            sum_pop += board[nx][ny]
                            visited[nx][ny] = True
                lands = list(set(lands))
                if len(lands) >= 2:
                    for x, y in lands:
                        _board[x][y] = sum_pop // len(lands)
    sum_row = 0
    for row in _board:
        sum_row += sum(row)
    if sum_row == 0:
        break
    cnt += 1
    for x in range(n):
        for y in range(n):
            if _board[x][y]:
                board[x][y] = _board[x][y]

print(cnt)


'''
정답 풀이
import sys
from _collections import deque

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(row, col):
    check = False
    visited = {(row, col)}
    q = deque([(row, col)])
    val, cnt = 0, 0

    while q:
        row, col = q.popleft()
        val += arr[row][col]
        cnt += 1
        for i in range(4):
            new_row, new_col = row + dy[i], col + dx[i]

            if 0 <= new_row < N and 0 <= new_col < N and (new_row, new_col) not in visited and L <= abs(arr[new_row][new_col] - arr[row][col]) <= R:
                q.append((new_row, new_col))
                visited.add((new_row, new_col))
                check = True
    return val // cnt, visited, check


def move():
    # 인구 이동
    cnt, pre_cnt = 0, 0
    while True:
        is_Move = False
        total_visited = set()
        temp = []
        for i in range(N):
            for j in range(N):
                if (i, j) not in total_visited:
                    value, visited, flag = bfs(i, j)
                    if flag:
                        is_Move = True
                    temp.append((value, visited))
                    total_visited |= visited

        for (value, visit) in temp:
            for y, x in visit:
                arr[y][x] = value
        if not is_Move:
            return cnt
        cnt += 1


if __name__ == "__main__":
    N, L, R = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(move())
'''