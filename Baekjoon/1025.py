from itertools import permutations


n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.extend(list(map(int, list(input()))))

answer = 0
for i in range(1, len(nums)+1):
    for perm in permutations(nums, i):
        num = int(''.join(list(map(str, perm))))
        if int(num ** (1/2)) == num ** (1/2):
            answer = max(answer, num)
print(answer)

print(answer ** (1/2))