from itertools import permutations
from copy import deepcopy
# import sys
# sys.stdin = open('14888.txt', 'r')


# 각 리스트당 계산 하기 (가지치기)
def cal(p, nums):
    global maxnum, minnum
    numslist = deepcopy(nums)
    ans = numslist.pop(0)
    for i in p:
        num = numslist.pop(0)
        if i == '+':
            ans += num
        elif i == '-':
            ans -= num
        elif i == '*':
            ans *= num
        elif i == '/':
            if ans < 0:
                ans = -(-ans // num)
            else:
                ans //= num
    if ans > maxnum:
        maxnum = ans
    if ans < minnum:
        minnum = ans


n = int(input())
nums = list(map(int, input().split()))
opnums = list(map(int, input().split()))
oplist = []
maxnum, minnum = -1000000000, 10000000000

# 연산자 갯수 만큼 연산자 리스트 만들기
for _ in range(opnums[0]):
    oplist.append('+')
for _ in range(opnums[1]):
    oplist.append('-')
for _ in range(opnums[2]):
    oplist.append('*')
for _ in range(opnums[3]):
    oplist.append('/')

# 연산자 순열 리스트
for p in permutations(oplist):
    cal(p, nums)

print(maxnum)
print(minnum)


'''
플러스
1. 재귀
2. from collections import deque
3. int(ans/num)
4. sys.maxsize == 10억

'''