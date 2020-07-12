import sys

sys.stdin = open('input1.txt','r')

num = int(input())

dx = [1, 0, -1, 0]   # 배열에서 쓸때는 x y 반대로
dy = [0, 1, 0, -1]

for i in range(num):
    N = int(input())
    ans = [[0] * N for _ in range(N)]
    x, y = 0, 0
    for j in range(N*N+1):
        ans[y][x] = j
        y += dy[l]
        x += dx[l]