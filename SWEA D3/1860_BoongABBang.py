import sys

sys.stdin = open('1860.txt', 'r')


T = int(input())
for i in range(T):
    n, m, k = list(map(int, input().split()))
    guests = sorted(list(map(int, input().split())))
    ans = 'Possible'
    for idx, guest in enumerate(guests):
        if (guest//m)*k - (idx+1) < 0:
            ans = 'Impossible'
            break
    print('#%d %s' % (i+1, ans))

#
# for idx in range(len(peoples)):
#         if (peoples[idx] // M)*K - (idx + 1) >= 0:

'''
T = int(input())
for i in range(T):
    n, m, k = list(map(int, input().split()))
    guest = sorted(list(map(int, input().split())))
    time = [0] * (sum(guest)+1)
    ans = 'Possible'
    for t in range(0, (sum(guest)+1), m):
        if t == 0:
            continue
        else:
            time[t] = k
    for t in guest:
        for bab in range(t+1):
            if sum(time[:t+1]) == 0:
                ans = 'Impossible'
                break
            if time[bab] != 0:
                time[bab] -= 1
                break
        if ans == 'Impossible':
            break

    print('#%d %s' % (i+1, ans))
'''