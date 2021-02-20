import sys
sys.stdin = open('10830.txt', 'r')

'''
# numpy 사용
import numpy as np

N, B = map(int, input().split(' '))

arr = [list(map(int, input().split(' '))) for _ in range(N)]
arr2 = arr

for _ in range(B-1):
    arr2 = np.dot(arr2, arr)

arr2 = arr2 % 1000
for row in arr2:
    print(' '.join(list(map(str, row))))
'''
# 행렬 곱셈
def mul(arr1, arr2, N):
    tmparr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += arr1[i][k] * arr2[k][j]
            tmparr[i][j] = tmp % 1000
    return tmparr

N, B = map(int, input().split(' '))

arr = [list(map(int, input().split(' '))) for _ in range(N)]

# 단위 행렬 만들기
rst = [[0] * N for _ in range(N)]
for i in range(N):
    rst[i][i] = 1

# B를 이진수로 만들어서 제곱하기
while B != 0:
    if B % 2:
        rst = mul(rst, arr, N)
    B >>= 1
    arr = mul(arr, arr, N)

# 출력
for row in rst:
    print(' '.join(list(map(str, row))))