import sys
sys.stdin = open('3349.txt', 'r')


T = int(input())
for tc in range(T):
    w, h, n = map(int, input().split())
    nodelist = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        if i == 0:
            continue
        else:
            xdiff = nodelist[i][0] - nodelist[i-1][0]
            ydiff = nodelist[i][1] - nodelist[i-1][1]
            while not (xdiff == 0 and ydiff == 0):
                if xdiff > 0 and ydiff > 0:
                    ans += 1
                    xdiff -= 1
                    ydiff -= 1
                elif xdiff > 0 and ydiff == 0:
                    ans += 1
                    xdiff -= 1
                elif xdiff == 0 and ydiff > 0:
                    ans += 1
                    ydiff -= 1
                elif xdiff > 0 and ydiff < 0:
                    ans += 2
                    xdiff -= 1
                    ydiff += 1
                elif xdiff < 0 and ydiff > 0:
                    ans += 2
                    xdiff += 1
                    ydiff -= 1
                elif xdiff < 0 and ydiff < 0:
                    ans += 1
                    xdiff += 1
                    ydiff += 1
                elif xdiff < 0 and ydiff == 0:
                    ans += 1
                    xdiff += 1
                elif xdiff == 0 and ydiff < 0:
                    ans += 1
                    ydiff += 1
    print('#%d %d' % (tc+1, ans))