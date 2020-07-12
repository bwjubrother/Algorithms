import sys
sys.stdin = open('4613.txt', 'r')


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    ip = [input() for _ in range(n)]
    minnum = float('inf')
    for i in range(1, n-1):
        for j in range(i+1, n):
            tmp = 0
            for white in ip[:i]:
                tmp += m - white.count('W')
            for blue in ip[i:j]:
                tmp += m - blue.count('B')
            for red in ip[j:]:
                tmp += m - red.count('R')
            if minnum > tmp:
                minnum = tmp
    print('#%d %d' % (tc+1, minnum))