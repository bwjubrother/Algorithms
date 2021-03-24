n, m = map(int, input().split())
nums = list(map(int, input().split()))
max_sum = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num_sum = nums[i] + nums[j] + nums[k]
            if num_sum > m:
                continue
            else:
                max_sum = max(max_sum, num_sum)
print(max_sum)