import sys
sys.stdin = open('17135.txt', 'r')

from heapq import heappush, heappop
from copy import deepcopy 

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# kill
def kill(board, archors):
    killed = 0
    _board = deepcopy(board)
    for _ in range(n):
        enemy = []
        for idx in range(3):
            q = []
            for i in range(n):
                for j in range(m):
                    if _board[i][j]:
                        dist = abs(n-i)+abs(archors[idx]-j)
                        if dist <= d:
                            heappush(q, (dist, j, i))
            if q:
                _, y, x = heappop(q)
                enemy.append((x, y))
        # kill (dist, j , i)
        for x, y in enemy:
            if _board[x][y]:
                _board[x][y] = 0
                killed += 1
        # move
        for i in range(n-1, 0, -1):
            for j in range(m):
                _board[i][j] = _board[i-1][j]
        for j in range(m):
            _board[0][j] = 0
    return killed

ans = 0
# archor location
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            archors = [i, j, k]
            ans = max(ans, kill(board, archors))

print(ans)