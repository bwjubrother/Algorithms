import sys
sys.stdin = open('1952.txt', 'r')


def find(idx, s):
    global minp
    if idx >= 12:
        if minp > s:
            minp = s
    else:
        find(idx+1, s+d*days[idx])
        find(idx+1, s+m)
        find(idx+3, s+mmm)


T = int(input())
for i in range(T):
    d, m, mmm, y = map(int, input().split())
    days = list(map(int, input().split()))
    minp = y
    find(0, 0)
    print('#%d %d' % (i+1, minp))

