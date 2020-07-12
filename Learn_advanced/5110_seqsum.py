import sys
sys.stdin = open('5110.txt', 'r')


T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    for j in range(m-1):
        ip = list(map(int, input().split()))
        for idx, k in enumerate(nums):
            if ip[0] < k:
                nums[idx:idx] = ip
                break
        else:
            nums += ip
    print('#%d %s' % (i+1, ' '.join(list(map(str, nums[-1:-11:-1])))))


