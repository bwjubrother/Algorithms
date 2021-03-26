t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    zero = [i for i in range(1, n+1)]
    for i in range(k):
        tmp = []
        for j in range(n):
            tmp.append(sum(zero[:j+1]))
        zero = tmp
    print(zero[n-1])