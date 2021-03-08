import sys
sys.stdin = open('14889.txt', 'r')


from itertools import combinations


def power(team):
    power_sum = 0
    for i in range(len(team)):
        for j in range(i, len(team)):
            power_sum += board[team[i]][team[j]]
            power_sum += board[team[j]][team[i]]
    return power_sum


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
people = [i for i in range(n)]
min_diff = 100
for team in combinations(people, n//2):
    start = list(team)
    link = list(set(people) - set(team))
    min_diff = min(min_diff, abs(power(start) - power(link)))
print(min_diff)