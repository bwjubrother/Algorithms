
def solution(board, moves):
    answer = 0
    yxboard = list(map(list, zip(*board)))
    for i in range(len(yxboard)):
        yxboard[i] = list(str(int(''.join(list(map(str, yxboard[i]))))))
    stack = []
    for move in moves:
        if yxboard[move-1]:
            pick = yxboard[move-1].pop(0)
            if not stack:
                stack.append(pick)
            else:
                if pick == stack[-1]:
                    stack.pop(-1)
                    answer += 2
                else:
                    stack.append(pick)
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

