import sys
sys.stdin = open('15686.txt', 'r')


from itertools import combinations


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# naive 방법

# 치킨집, 집 찾기
houses = []
chickens = []
for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            houses.append((x, y))
        if board[x][y] == 2:
            chickens.append((x, y))

min_dist = float('inf')
# 치킨집 중 M개를 고른다. (13Cm = 13^6)
for choose in combinations(chickens, m):
    dist_sum = 0
    # 집들을 돌면서 최소 거리들을 합한다. (100)
    for hx, hy in houses:
        close = 2*n
        for cx, cy in choose:
            close = min(close, abs(hx-cx)+abs(hy-cy))
        dist_sum += close
    min_dist = min(min_dist, dist_sum)

print(min_dist)