def solution(board, moves):
    answer = 0
    stack = []
    # 스택
    for move in moves:
        pick = 0
        for depth in range(len(board)):
            if board[depth][move-1] != 0:
                pick = board[depth][move-1]
                board[depth][move-1] = 0
                break
        if len(stack) > 0 and stack[-1] == pick:
            stack.pop(-1)
            answer += 2
        elif pick > 0:
            stack.append(pick)
    return answer