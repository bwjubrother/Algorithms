sen = str(input())

front = ord(sen[0])
answer = 1
for s in sen[1:]:
    if front >= ord(s):
        answer += 1
    front = ord(s)

print(answer)
