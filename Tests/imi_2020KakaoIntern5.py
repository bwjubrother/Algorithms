'''
# 1
def solution(stones, k):
    answer = 0
    while True:
        strstones = ''.join(list(map(str, stones)))
        if '0'*k in strstones:
            break
        answer += 1
        for i in range(len(stones)):
            if stones[i] > 0:
                stones[i] -= 1
    return answer
'''


# 2
def solution(stones, k):
    answer = 200000000
    for i in range(len(stones)-k+1):
        if max(stones[i:i+k]) < answer:
            answer = max(stones[i:i+k])
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
