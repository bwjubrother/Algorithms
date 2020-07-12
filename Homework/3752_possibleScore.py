import sys
sys.stdin = open('3752.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    scores = list(map(int, input().split()))
    cases = [0] * 10001
    idx, ans = 0, 1
    for score in scores:
        idx += score
        for case in cases[idx:0:-1]:
            if case:
                cases[case+score] = case+score
        cases[score] = score
    for case in cases[:idx+1]:
        if case:
            ans += 1
    print('#%d %d' % (tc+1, ans))