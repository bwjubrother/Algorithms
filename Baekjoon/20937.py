from collections import Counter


n = int(input())
nums = list(map(int, input().split(' ')))

num_dict = Counter(nums)
print(max(num_dict.values()))