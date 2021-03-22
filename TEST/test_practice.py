# 1번
def dfs(left, earnings, last):
    global max_earnings
    for jongmok in range(last + 1, N):
        if price[jongmok][month] < price[jongmok][month + 1]:
            stock = 1
            while left >= price[jongmok][month] * stock:
                dfs(left - price[jongmok][month] * stock, earnings + stock * (price[jongmok][month + 1] - price[jongmok][month]), jongmok)
                stock += 1
        if max_earnings < earnings:
            max_earnings = earnings

T = int(input())

for tc in range(1, T + 1):

    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    price = [list(map(int, input().split())) for _ in range(N)]

    now = Ms - Ma
    
    for month in range(L):
        now += Ma
        max_earnings = -1
        dfs(now, 0, -1)
        if max_earnings > 0:
            now += max_earnings

    print('#%d %d' % (tc, now - (Ms + Ma + (L - 1))))