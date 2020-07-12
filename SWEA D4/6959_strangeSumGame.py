import sys
sys.stdin = open('6959.txt', 'r')


T = int(input())
for tc in range(T):
    nums = str(input())
    cnt = 0
    while len(nums) != 1:
        nums = nums.replace(nums[0:2], str(int(nums[0]) + int(nums[1])), 1)
        cnt += 1
    if cnt % 2:
        winner = 'A'
    else:
        winner = 'B'
    print('#%d %s' % (tc+1, winner))


'''
for tc in range(int(input())):
    D = input()
    if ((sum(map(int, D))-1)//9+len(D))%2: res = 'B'
    else: res = 'A'
    print('#{} {}'.format(tc+1, res))
'''