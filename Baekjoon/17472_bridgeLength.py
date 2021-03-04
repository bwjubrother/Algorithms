import sys
sys.stdin = open('17472.txt', 'r')

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 다리의 갯수는 섬 갯수 - 1
# 각 섬마다 거리를 계산 (길이 2이상)

# 가장 긴 거 빼고 선택