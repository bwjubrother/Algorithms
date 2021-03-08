import sys
sys.stdin = open('13458.txt', 'r')


from math import ceil

n = int(input())
nums = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0
for num in nums:
    num -= b
    result += 1
    if num > 0:
        result += ceil(num / c)
print(result)