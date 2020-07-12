#1
opens = ['(', '{', '[', '<']
def solution(inputString):
    answer = 0
    openList = []
    for s in inputString:
        if s in opens:
            openList.append(s)
        if s == ')':
            if '(' in openList:
                openList.remove('(')
                answer += 1
            else:
                answer = -1
                break
        if s == '}':
            if '{' in openList:
                openList.remove('{')
                answer += 1
            else:
                answer = -1
                break
        if s == ']':
            if '[' in openList:
                openList.remove('[')
                answer += 1
            else:
                answer = -1
                break
        if s == '>':
            if '<' in openList:
                openList.remove('<')
                answer += 1
            else:
                answer = -1
                break
    if openList:
        answer = -1
    return answer

#2
def getDiff(s1, s2):
    tmp = ''
    for i in range(len(s1)):
        if s1[i] == s2[i] == '1':
            tmp += '1'
        else:
            tmp += '0'
    tcount, maxcount = 0, 0
    for j in tmp:
        if j == '1':
            tcount += 1
        if j == '0':
            if maxcount < tcount:
                maxcount = tcount
                tcount = 0
    return tmp.count('1') + maxcount**2

def solution(answer_sheet, sheets):
    answer = -1
    diffs = []
    for sheet in sheets:
        tmp = ''
        for i in range(len(answer_sheet)):
            if answer_sheet[i] == sheet[i]:
                tmp += '0'
            else:
                tmp += '1'
        diffs.append(tmp)
    maxDiff = 0
    for idx, diff in enumerate(diffs):
        for tdiff in diffs[idx+1:]:
            if getDiff(diff, tdiff) > maxDiff:
                maxDiff = getDiff(diff, tdiff)
    answer = maxDiff
    return answer

#3
def getLength(s):
    tmp, Length = 0, 0
    for i in s:
        if i == '1':
            tmp += 1
        elif tmp > Length:
            Length = tmp
            tmp = 0
    if tmp > Length:
        Length = tmp
    return Length


def solution(road, n):
    answer = -1
    maxL = 0
    for idx in range(len(road)):
        trans = road[idx:].replace('0', '1', n)
        if getLength(road[:idx] + trans) > maxL:
            maxL = getLength(road[:idx] + trans)
    answer = maxL
    return answer

#4
def solution(snapshots, transactions):
    answer = []
    ids = []
    snapDict = {}
    for snap in snapshots:
        snapDict[snap[0]] = int(snap[1])
    for trans in transactions:
        if trans[0] in ids:
            continue
        else:
            ids.append(trans[0])
            if trans[1] == 'SAVE':
                if trans[2] in snapDict.keys():
                    snapDict[trans[2]] += int(trans[3])
                else:
                    snapDict[trans[2]] = int(trans[3])
            elif trans[1] == 'WITHDRAW':
                snapDict[trans[2]] -= int(trans[3])
    for key, value in snapDict.items():
        answer.append([key, str(value)])
    answer.sort()
    return answer

#5
def solution(dataSource, tags):
    answer = []
    numDict = {}
    for data in dataSource:
        for tag in tags:
            if tag in data[1:]:
                if data[0] in numDict.keys():
                    numDict[data[0]] += 1
                else:
                    numDict[data[0]] = 1
    sortDict = sorted(numDict.items(), key=lambda x: x[1], reverse=True)
    for i in sortDict:
        answer.append(i[0])
    return answer



#6
def solution(directory, command):
    answer = []
    for c in command:
        tmp = c.split(' ')
        if tmp[0] == 'mkdir':
            directory.append(tmp[1])
        elif tmp[0] == 'cp':
            for d in directory:
                if d.startswith(tmp[1]):
                    directory.append(tmp[2]+d)
        elif tmp[0] == 'rm':
            tmpList = []
            for d in directory:
                if not d.startswith(tmp[1]):
                    tmpList.append(d)
            directory = tmpList
    answer = directory
    return answer