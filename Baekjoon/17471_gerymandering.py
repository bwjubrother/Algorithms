# case4 - 9
import sys
sys.stdin = open('17471.txt', 'r')

from itertools import combinations

# 두 개가 인접한 지 판단
def adjacent(group):
    q = []
    q.append(group[0])
    count = 1
    visited = []
    while q:
        loc = q.pop()
        visited.append(loc)
        for x in graph[loc]:
            if x in group and x not in visited:
                q.append(x)
                visited.append(x)
                count += 1
    if count == len(group):
        return True
    return False


# 두 개의 합의 차이 계산
def sumDiff(a, b):
    sumA, sumB = 0, 0
    for i in a:
        sumA += nums[i-1]
    for i in b:
        sumB += nums[i-1]
    return abs(sumA-sumB)


n = int(input())
nums = list(map(int, input().split()))
graph = [[]]
for _ in range(n):
    graph.append(list(map(int, input().split()))[1:])

# 두 개로 나눔
min_diff = float('inf')
location = [i for i in range(1, n+1)]
for i in range(1, n//2 + 1):
    for comb in combinations(location, i):
        a = list(comb)
        b = list(set(location) - set(a))
        if adjacent(a) and adjacent(b):
            min_diff = min(min_diff, sumDiff(a, b))
        else:
            continue

print(min_diff) if min_diff != float('inf') else print(-1)
