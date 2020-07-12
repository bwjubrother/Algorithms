import sys
sys.stdin = open('7465.txt', 'r')


def rep(num):
    while num != node[num]:
        num = node[num]
    return num


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    node = [i for i in range(n+1)]
    for j in range(m):
        left, right = map(int, input().split())
        node[rep(right)] = rep(left)
    cnt = 0
    for k in range(1, n+1):
        if k == node[k]:
            cnt += 1
    print('#%d %d' % (tc+1, cnt))
