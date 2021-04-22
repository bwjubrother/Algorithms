
# nums = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6}
nums = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [6, 0, 9], 7: [8]}
# smallest = {8: 10, 9: 18, 10: 22, 11: 20, 12: 28, 13: 68, 14: 88}
smallest = ['', '', '1', '7', '4', '2', '0', '8', '10']

T = int(input())

for _ in range(T):
    n = int(input())
    small, large = '', ''
    # 가장 작은 수
    if n in nums:
        small = str(nums[n][0])
    else:
        for i in range(len(smallest)+1, n+1):
            tmp = []
            for j in range(2, 9):
                tmp.append(int(smallest[i-j]+smallest[j]))
                tmp.append(int(smallest[j]+smallest[i-j]))
            smallest.append(str(min(tmp)))
        small = smallest[n]
    # 가장 큰 수
    while n > 0:
        if n == 3:
            large = '7' + large
            break
        else:
            large = '1' + large
            n -= 2
    print(small + ' ' + large)

# 8: 10, 9: 18, 10: 40, 11: 20, 12: 28, 13: 68, 14: 88 