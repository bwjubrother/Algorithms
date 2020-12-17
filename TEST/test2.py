import sys
sys.stdin = open('test2.txt', 'r')


def main(t):
    N, R = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if maps[x][y] == 9:
                for dx in range(R + 1):
                    if 0 <= x + dx < N and 0 <= y + R - dx < N:
                        maps[x + dx][y + R - dx] = -1
                    if 0 <= x - dx < N and 0 <= y - R + dx < N:
                        maps[x - dx][y - R + dx] = -1

    ans = 1

    print('#%d %d' % (t + 1, ans))


if __name__ == "__main__":

    T = int(input())

    for t in range(T):
        main(t)
