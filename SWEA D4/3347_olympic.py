import sys
sys.stdin = open('3347.txt', 'r')


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    vote = [0] * n
    for person in mlist:
        for cost in nlist:
            if cost <= person:
                vote[nlist.index(cost)] += 1
                break
    ans = vote.index(max(vote))+1
    print('#%d %d' % (tc+1, ans))