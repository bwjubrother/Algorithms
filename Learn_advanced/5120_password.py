import sys
sys.stdin = open('5210.txt', 'r')


T = int(input())
for tc in range(T):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    location = 0
    length = n
    for _ in range(k):
        location = (location + m) % length
        if location == length:
            nums.insert(location, nums[location-1] + nums[0])
        elif location == 0:
            nums.append(nums[-1] + nums[location])
            location -= 1
        else:
            nums.insert(location, nums[location-1] + nums[location])
        length += 1
    print('#%d %s' % (tc+1, ' '.join(list(map(str, nums[-1:-11:-1])))))
