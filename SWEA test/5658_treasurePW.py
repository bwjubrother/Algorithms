import sys
sys.stdin = open('5658.txt', 'r')


T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    ip = input()
    div = n // 4
    pws = set()
    for i in range(div):
        for j in range(0, n, div):
            pws.add(ip[j:j+div])
        tmp = ip[-1]
        ip = ip[::-1].replace(ip[-1], '', 1)
        ip = tmp + ip[::-1]
    pws = sorted(pws, reverse = True)
    print('#%d %d' % (tc+1, int(pws[k-1], 16)))