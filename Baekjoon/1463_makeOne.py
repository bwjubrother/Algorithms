
N = int(input())
ans = float('inf')

# 1 -> 0, 2 -> 1, 3 -> 1
arr = [0, 0, 1, 1]
for i in range(4, N+1):
    three, two, one = float('inf'), float('inf'), arr[i-1]
    if not i % 3:
        three = arr[i // 3]
    if not i % 2:
        two = arr[i // 2]
    arr.append(1 + min(three, two, one))

print(arr[N])
       