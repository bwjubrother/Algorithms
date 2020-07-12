import sys
sys.stdin = open('5189.txt', 'r')


def go(k, route):
    if k == n:
        routes.append(route+[0])
        return
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            go(k+1, route+[arr[k]])
            arr[i], arr[k] = arr[k], arr[i]

T = int(input())
for tc in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    arr = [i for i in range(n)]
    routes = []
    go(1, [0])
    minS = float('inf')
    for route in routes:
        s = 0
        for idx in range(n):
            s += board[route[idx]][route[idx+1]]
        if s < minS:
            minS = s
    print('#%d %d' % (tc+1, minS))

