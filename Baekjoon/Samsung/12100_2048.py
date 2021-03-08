import sys
sys.stdin = open('2048.txt', 'r')


from copy import deepcopy


def findMax(board):
    block = 0
    for row in board:
        for item in row:
            if item and item > block:
                block = item
    return block


def move(board):
    new_board = [[0] * len(board[0]) for _ in range(len(board))]
    for x in range(len(board)):
        block = 0
        idx = 0
        for y in range(len(board[0])):
            if board[x][y]:
                if block:
                    if block == board[x][y]:
                        new_board[x][idx] = 2 * block
                        idx += 1
                        block = 0
                    else:
                        new_board[x][idx] = block
                        idx += 1
                        block = board[x][y]
                else:
                    block = board[x][y]
        if block:
             new_board[x][idx] = block
    return new_board


def play(board, turn):
    global max_block
    if turn == 5:
        max_block = max(max_block, findMax(board))
        return
    else:
        _board = deepcopy(board)
        # 좌로 이동
        play(move(_board), turn+1)
        # 우로 이동
        r_board = [row[::-1] for row in _board]
        play(move(r_board), turn+1)
        # 위로 이동
        u_board = list(map(list, zip(*_board)))
        play(move(u_board), turn+1)
        # 아래로 이동
        d_board = [row[::-1] for row in u_board]
        play(move(d_board), turn+1)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 5번의 실행
# 실행은 상하좌우 모두 해본다. 실행 + 1
# 실행이 5 되었을때 최대값을 비교, 갱신한다.
max_block = 0
play(board, 0)
print(max_block)