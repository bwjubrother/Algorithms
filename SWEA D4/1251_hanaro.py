import sys
sys.stdin = open('1251.txt')


T = int(input())
for tc in range(T):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    # 계산식 : E * L^2   의 int
    