import sys
sys.stdin = open('4012.txt', 'r')


def comb(k, n, a, b):
    global mint
    if k == n:
        tmp = abs(taste(A, n) - taste(B, n))
        if tmp < mint:
            mint = tmp
    else:
        if a < n//2:
            A.append(k)
            comb(k+1, n, a+1, b)
            A.pop()
        if b < n//2:
            B.append(k)
            comb(k+1, n, a, b+1)
            B.pop()

def taste(arr, n):
    s = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            s += tastes[arr[i]][arr[j]]
            s += tastes[arr[j]][arr[i]]
    return s

T = int(input())
for tc in range(T):
    n = int(input())
    tastes = [list(map(int, input().split())) for _ in range(n)]
<<<<<<< HEAD
    lendiv = n // 2
    # 2개로 나누는 조합
    arr = [i for i in range(n)]
    combs = []
    comb(n, 0, [])
    print(combs)
    # 그 집합내에서 2개씩 뽑는 순열
=======
    A, B = [], []
    mint = float('inf')
    comb(0, n, 0, 0)
    print('#%d %d' % (tc+1, mint))
>>>>>>> 41e0dba01233ac1b1bfbf88a717d3ef8988b9173
