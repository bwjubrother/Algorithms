import sys
sys.stdin = open('5201.txt', 'r')


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    ns = list(map(int, input().split()))
    ms = list(map(int, input().split()))
    ans = 0
    while ns and ms:
        if max(ns) <= max(ms):
            ans += max(ns)
            ns.remove(max(ns))
            ms.remove(max(ms))
        else:
            ns.remove(max(ns))
    print('#%d %d' % (tc+1, ans))