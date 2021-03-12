import sys
sys.stdin = open('15684.txt', 'r')


def check():
    for start in range(n):
        k = start
        for i in range(h):
            if ladder[i][k]:
                k += 1
            elif k > 0 and ladder[i][k-1]:
                k -= 1
        if start != k:
            return False
    return True


def bfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n-1):
            if not ladder[i][j] and not ladder[i][j+1]:
                ladder[i][j] = True
                bfs(cnt+1, i, j+2)
                ladder[i][j] = False


n, m, h = map(int, input().split())
ladder = [[False] * n for _ in range(h)]
for _ in range(m):
    x, y = map(int, input().split())
    ladder[x-1][y-1] = True

# cnt > 3 and impossible , print(-1)
ans = 4
bfs(0, 0, 0)
print(ans if ans < 4 else -1)
