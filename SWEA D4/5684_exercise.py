import sys
sys.stdin = open('5684.txt', 'r')


# 리스트로 구현.
def dfs(now, sum, start, check):
    global ans
    check[now] = 1
    for i in route[now]:
        next = i[0]
        cost = i[1]
        if not check[next] and ans > sum + cost:
            dfs(next, sum+cost, start, check)
        if start == next:
            if ans > sum+cost:
                ans = sum+cost


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    route = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, c = map(int, input().split())
        route[s].append([e, c])
    ans = float('inf')
    for i in range(1, n+1):
        dfs(i, 0, i, [0]*(n+1))
    if ans == float('inf'):
        ans = -1
    print('#%d %d' % (tc+1, ans))