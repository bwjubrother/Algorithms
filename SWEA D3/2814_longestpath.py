import sys
sys.stdin = open('2814.txt', 'r')


def dfs(s, l):
    visited[s] = 1
    results.append(l)
    for k in a[s]:
        if not visited[k]:
            dfs(k, l+1)
            visited[k] = 0

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    a = [[] for _ in range(n+1)]
    results = []
    for i in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    for j in range(n):
        visited = [0]*(n+1)
        dfs(j, 1)
    print('#%d %d' % (tc+1, max(results[:])))