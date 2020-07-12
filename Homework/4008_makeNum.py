import sys
sys.stdin = open('4008.txt', 'r')


'''
def cal(ops, nums):
    global cals
    tmp = 0
    for idx, num in enumerate(nums):
        if not idx:
            tmp = num
        else:
            if ops[idx-1] == '+':
                tmp = tmp + num
            elif ops[idx-1] == '-':
                tmp = tmp - num
            elif ops[idx-1] == '*':
                tmp = tmp * num
            elif ops[idx-1] == '/':
                tmp = int(tmp / num)
    cals.append(tmp)


def perm(ops, k, n):
    if k == n:
        cal(ops, nums)
    else:
        for j in range(k, n):
            ops[k], ops[j] = ops[j], ops[k]
            perm(ops, k+1, n)
            ops[k], ops[j] = ops[j], ops[k]

T = int(input())
for i in range(T):
    n = int(input())
    opNums = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ops = ['+'] * opNums[0]
    ops += ['-'] * opNums[1]
    ops += ['*'] * opNums[2]
    ops += ['/'] * opNums[3]
    cals = []
    perm(ops, 0, len(ops))
    ans = max(cals) - min(cals)
    print('#%d %d' % (i+1, ans))
'''


'''
def cal(ops, nums):
    global cals, maxcal, mincal
    tmp = 0
    for idx, num in enumerate(nums):
        if not idx:
            tmp = num
        else:
            if ops[idx-1] == '+':
                tmp = tmp + num
            elif ops[idx-1] == '-':
                tmp = tmp - num
            elif ops[idx-1] == '*':
                tmp = tmp * num
            elif ops[idx-1] == '/':
                tmp = int(tmp / num)
    if tmp > maxcal:
        maxcal = tmp
    if tmp < mincal:
        mincal = tmp


def perm(ops, k, n):
    global calperm
    if k == n:
        if ops not in calperm:
            calperm.append(ops)
    else:
        for j in range(k, n):
            ops[k], ops[j] = ops[j], ops[k]
            perm(ops[:], k+1, n)
            ops[k], ops[j] = ops[j], ops[k]

T = int(input())
for i in range(T):
    n = int(input())
    opNums = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ops = ['+'] * opNums[0]
    ops += ['-'] * opNums[1]
    ops += ['*'] * opNums[2]
    ops += ['/'] * opNums[3]
    calperm = []
    perm(ops, 0, len(ops))
    maxcal = 0
    mincal = float('inf')
    for cp in calperm:
        cal(cp, nums)
    ans = maxcal - mincal
    print('#%d %d' % (i+1, ans))
'''


def my_perm(calcs):
    stack = [(calcs[:], [])]  # 남은 연산자, 리턴할 결과
    while stack:
        my_calc, temp = stack.pop()
        if sum(my_calc) == 0:
            yield temp
        for i in range(4):
            if my_calc[i]:
                my_calc[i] -= 1
                temp.append(i)
                stack.append((my_calc[:], temp[:]))
                temp.pop()
                my_calc[i] += 1


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    calc = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    my_min = float('inf')
    my_max = -float('inf')

    # 연산자로 만들 수 있는 경우의 수
    for perm in my_perm(calc):
        idx = 0
        sub_res = nums[idx]
        # 계산
        for cal in perm:
            idx += 1
            if cal == 0:
                sub_res += nums[idx]
            elif cal == 1:
                sub_res -= nums[idx]
            elif cal == 2:
                sub_res *= nums[idx]
            elif cal == 3:  # 음수에서 소수점 버릴 때 주의
                # upper = 1 if sub_res < 0 and sub_res % nums[idx] else 0
                # sub_res //= nums[idx]
                # sub_res += upper
                sub_res = int(sub_res / nums[idx])
        # 결과 갱신
        if sub_res < my_min:
            my_min = sub_res
        if sub_res > my_max:
            my_max = sub_res

    print('#{} {}'.format(test_case, my_max - my_min))