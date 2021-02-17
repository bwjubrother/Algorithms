import sys
sys.stdin = open('1181.txt', 'r')

N = int(input())
words = []
for _ in range(N):
    words.append(input())

words = list(set(words))
words.sort(key = lambda x : (len(x), x))

for i in range(len(words)):
    print(words[i])