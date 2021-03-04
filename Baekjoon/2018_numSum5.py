
n = int(input())
cnt = 0
for i in range(1, n//2 + 1):
    nsum = 0
    for j in range(i, n//2 + 2):
        nsum += j
        if nsum == n:
            cnt += 1
            break
        elif nsum > n:
            break
print(cnt+1)