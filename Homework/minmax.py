ip = int(input())
num = []
numbers = []
ans = []

for i in range(ip):
    num.append(int(input()))
    numbers.append(list(map(int, input().split())))

for number in numbers:
    max = number[0]
    min = number[0]
    for j in number[1:]:
        if j > max:
            max = j
        if j < min:
            min = j
    ans.append(max - min)

for i in range(ip):
    print('#%d %d' % (i + 1, ans[i]))
