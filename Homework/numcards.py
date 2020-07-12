num = int(input())
case = []
number = []
ans = []

for i in range(num):
    case.append(int(input()))
    number.append(list(input()))

for j in number:
    counts = [0] * 10
    tmp = []
    for k in j:
        counts[int(k)] += 1
    for o, u in enumerate(counts):
        if int(u) == max(counts):
            tmp.append(o)
    ans.append([max(tmp), max(counts)])

for l in range(num):
    print('#%d %d %d' % ((l + 1), ans[l][0], ans[l][1]))
    