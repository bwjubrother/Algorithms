T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    nums = input().split()
    for j in range(m):
        nums.append(nums.pop(0))
    print('#%d %s' %(i+1, nums[0]))