import sys
sys.stdin = open('14890.txt', 'r')

def slope(i, c):
    global ans
    cnt = 1
    for j in range(0, N-1):
        # 높이 차이
        d = a[i][j+1]-a[i][j] if c else a[j+1][i]-a[j][i]
        # 높이가 동일하면 cnt += 1
        if d == 0:
            cnt += 1
        # 높이가 더 높으면 cnt가 l이상 확보되어야 한다.
        elif d == 1 and cnt >= L:
            cnt = 1
        # 높이가 더 낮으면 cnt가 l만큼 필요하기 때문에 cnt = -l+1로 초기화, 
        elif d == -1 and cnt >= 0:
            cnt = -L+1
        # 높이가 높거나 낮을때 후자 조건이 만족되지 않으면 불가능
        else:
            return
    # cnt가 0이상이어야 필요한 경사가 없다.
    if cnt >= 0:
        ans += 1

def solve():
    for i in range(N):
        # 행방향, 열방향 탐색
        slope(i, 1)
        slope(i, 0)
    print(ans)

N, L = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
ans = 0
solve()
