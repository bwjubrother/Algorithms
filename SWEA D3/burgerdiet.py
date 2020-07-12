T = int(input())

def partset(arr, n):
    sets = []
    for j in range(1<<n):
        tmp = []
        for k in range(n):
            if j & (1<<k):
                tmp.append(arr[k])
        if int(sum(tmp)) < l:
            sets.append(tmp)
    return sets

for i in range(T):
    n, l = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    cal_taste = {}
    for j in nums:
        if j[1] in cal_taste.keys():
            cal_taste[j[1] + 0.1] = j[0]
        else:
            cal_taste[j[1]] = j[0]
    cals = partset(list(cal_taste.keys()), n)
    ans = 0
    for k in cals:
        tmp = 0
        for l in k:
            tmp += cal_taste[l]
        if ans < tmp:
            ans = tmp
    print('#%d %d' % (i+1, ans))
    # ans = []
    # for j in range(n):
    #     taste, cal = 0, 0
    #     for k in range(j, n):
    #         cal += nums[k][1]
    #         if cal > l:
    #             break
    #         taste += nums[k][0]
    #     print(taste, cal)
    #     ans.append(taste)
    # print('#%d %d' %(i+1, max(ans)))