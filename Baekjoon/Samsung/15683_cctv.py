import sys
sys.stdin = open('15683.txt', 'r')


n, m = map(int, input().split())
# 1번은 한쪽, 2번은 양쪽, 3번은 ㄱ자, 4번은 3방향, 5번은 4방향, 6번 벽
# 사각지대의 최소 크기 = 최소 0의 갯수
board = [list(map(int, input().split())) for _ in range(n)]
for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            