def solution(s):
    answer = []
    slist =  s.replace('{','')[:-2].split('},')
    for idx, nums in enumerate(slist):
        slist[idx] = nums.split(',')
    length = 1
    while length <= len(slist):
        for num in slist:
            if len(num) == length:
                for n in num:
                    if int(n) not in answer:
                        answer.append(int(n))
                        break
        length += 1
    return answer