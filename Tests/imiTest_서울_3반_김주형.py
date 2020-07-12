import sys
sys.stdin = open('test.txt', 'r')


dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def inside(x, y):
    if 0 <= x < 10 and 0 <= y < 10:
        return True
    return False

T = int(input())
for tc in range(T):
    sky = [list(map(int, input().split())) for _ in range(10)]
    visited = [[0] * 10 for _ in range(10)]
    ans = 0
    for x in range(10):
        for y in range(10):
            if not visited[x][y] and sky[x][y]:
                ans += 1
                stack = [(x, y)]
                while stack:
                    nx, ny = stack.pop()
                    visited[nx][ny] = 1
                    for i in range(8):
                        newx = nx + dx[i]
                        newy = ny + dy[i]
                        if inside(newx, newy) and not visited[newx][newy] and sky[newx][newy]:
                            stack.append((newx, newy))
                            visited[newx][newy] = 1
    print('#%d %d' % (tc + 1, ans))
