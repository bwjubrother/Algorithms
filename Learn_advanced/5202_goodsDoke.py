import sys
sys.stdin = open('5202.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    worktimes = [list(map(int, input().split())) for _ in range(n)]
    worktimes.sort()
    time, ans = worktimes[0][1], 1
    for worktime in worktimes[1:]:
        if worktime[0] >= time:
            time = worktime[1]
            ans += 1
        else:
            if worktime[1] < time:
                time = worktime[1]
    print('#%d %d' % (tc+1, ans))
