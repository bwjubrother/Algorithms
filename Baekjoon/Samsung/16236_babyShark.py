import sys
sys.stdin = open('16236.txt', 'r')


def eat(feed, shark):
    global board, ans, sx, sy
    ate = 0
    while food[feed]:
        min_dist = 2*n
        min_x, min_y = n, n
        for fx, fy in food[feed]:
            if min_dist > abs(fx-sx)+abs(fy-sy):
                if x < min_x:
                    if y < min_y:
                        min_dist = abs(fx-sx)+abs(fy-sy)
                        min_x, min_y = x, y
        ate += 1
        ans += min_dist
        food[feed].remove((min_x, min_y))
        sx, sy = min_x, min_y
        if ate == shark:
            break
    return


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 위치 찾기
food = [[] for _ in range(7)]
for x in range(n):
    for y in range(n):
        if board[x][y] == 9:
            sx, sy = x, y
        elif board[x][y] and board[x][y] != 9:
            food[board[x][y]].append((x, y))

print(food)
ans = 0
for i in range(1, 7):
    eat(i, 2)
print(ans)
            