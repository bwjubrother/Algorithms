import sys
from collections import Counter


n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

avg = round(sum(nums) / n)
print(avg)

nums.sort()
mid = nums[n//2]
print(mid)

cnts = Counter(nums).most_common()
# for num in nums:
#     cnts.append((nums.count(num), num))
# cnts.sort(key = lambda x : (-x[0], x[1]))
if n > 1:
    if cnts[0][1] == cnts[1][1]:
        print(cnts[1][0])
    else:
        print(cnts[0][0])
else:
    print(nums[0])

rng = max(nums) - min(nums)
print(rng)