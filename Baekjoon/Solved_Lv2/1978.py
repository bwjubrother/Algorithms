
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n//2+1):
        if not n % i:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    if isPrime(num):
        cnt += 1
print(cnt)