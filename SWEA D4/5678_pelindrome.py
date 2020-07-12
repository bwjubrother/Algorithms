import sys
sys.stdin = open('5678.txt', 'r')


T = int(input())
for tc in range(T):
    sen = input()
    ans = -1
    if len(sen) == 1:
        ans = 1
    for i, letter in enumerate(sen):
        for j in range(len(sen)-1, i, -1):
            if letter == sen[j]:
                mid = (j - i + 1) // 2
                if sen[i:i+mid] == sen[j:j-mid:-1]:
                    if ans < j - i + 1:
                        ans = j - i + 1
    print('#%d %d' % (tc+1, ans))
