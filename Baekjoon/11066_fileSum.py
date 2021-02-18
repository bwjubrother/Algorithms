import sys
sys.stdin = open('11066.txt', 'r')

T = int(input())
for _ in range(T):
    K = int(input())
    arr = [int(x) for x in input().split()]
    rst = [[0 for _ in range(K)] for _ in range(K)]
    for j in range(1, K):
        for i in range(j-1, -1, -1):
            small = float('inf')
            for k in range(j-i):
                small = min(small, rst[i][i+k] + rst[i+k+1][j])
            rst[i][j] = small + sum(arr[i:j+1])
    print(rst[0][K-1])
