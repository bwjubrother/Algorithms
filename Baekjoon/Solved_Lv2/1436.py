n = int(input())

movie = 666
cnt = 0
while True:
    if '666' in str(movie):
        cnt += 1 
    if cnt == n:
        break
    movie += 1

print(movie)