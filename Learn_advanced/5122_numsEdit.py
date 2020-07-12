import sys
sys.stdin = open('5122.txt', 'r')


T = int(input())
for tc in range(T):
    n, m, l = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(m):
        ip = input().split()
        if ip[0] == 'I':
            nums.insert(int(ip[1]), int(ip[2]))
        elif ip[0] == 'D':
            nums.pop(int(ip[1]))
        elif ip[0] == 'C':
            nums[int(ip[1])] = int(ip[2])
    try:
        print('#%d %d' % (tc+1, nums[l]))
    except IndexError:
        print('#%d %d' % (tc+1, -1))