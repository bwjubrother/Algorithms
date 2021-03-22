def solution(number, k):
    answer = 0
    stack = []
    for num in number:
        if not stack:
            stack.append(num)
        elif stack[-1] >= num and not k:
            stack.append(num)
        else:
            while stack[-1] < num and k:
                stack.pop(-1)
                k -= 1
                if not stack:
                    break
            stack.append(num)
    answer = ''.join(stack)
    return answer

print(solution("987654321",8))