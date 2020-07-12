import sys
sys.stdin = open('1219.txt', 'r')


def dfs(now):
    global ans
    if ans == 1:
        return
    if now == 99:
        ans = 1
    for i in nodes[now]:
        dfs(i)

for _ in range(10):
    num, n = map(int, input().split())
    nlist = list(map(int, input().split()))
    nodes = [[] for _ in range(100)]
    for i in range(0, 2*n, 2):
        nodes[nlist[i]].append(nlist[i+1])
    ans = 0
    dfs(0)
    print('#%d %d' % (num, ans))