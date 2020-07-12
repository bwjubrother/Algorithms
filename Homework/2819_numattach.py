import sys
sys.stdin = open('2819.txt', 'r')


delta = ((1, 0), (-1, 0), (0, 1), (0, -1))


def find(x, y):
    global nums, ans
    nums.append(board[x][y])
    print(nums)
    if len(nums) == 3:
        if nums not in ans:
            ans.append(nums)
        nums = []
        return

    for i in range(4):
        newx = x + delta[i][0]
        newy = y + delta[i][1]
        if 0<=newx<4 and 0<=newy<4:
            find(newx, newy)


T = int(input())
for tc in range(T):
    board = [list(map(int, input().split())) for _ in range(4)]
    nums = []
    ans = []
    for x in range(4):
        for y in range(4):
            find(x, y)
    print(len(ans))