import sys
sys.stdin = open('13460.txt', 'r')

n, m = map(int, input().split())

# 좌 (0, -1) 우 (0, 1) 위 (-1, 0) 아래(1, 0)