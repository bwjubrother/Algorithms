import sys
sys.stdin = open('2805.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    ground = [list(map(int, input())) for _ in range(n)]
    center = n//2
    d, ans = 0, 0
    for x in ground[:center]:
        ans += sum(x[center-d:center+d+1])
        d += 1
    ans += sum(ground[center])
    for x in ground[center+1:]:
        d -= 1
        ans += sum(x[center-d:center+d+1])
    print('#%d %d' % (tc+1, ans))