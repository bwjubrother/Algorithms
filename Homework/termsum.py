num = int(input())

for i in range(num):
    cases = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    tmp = []

    for j in range(cases[1] - 1, cases[0]):
        sum = 0
        for k in range(cases[1]):
            sum += numbers[j - k]
        tmp.append(sum)
    print('#%d %d' % (i + 1, max(tmp) - min(tmp)))
