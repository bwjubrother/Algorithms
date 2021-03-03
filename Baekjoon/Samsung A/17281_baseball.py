import sys
sys.stdin = open('17281.txt', 'r')

from itertools import permutations

# case4 - res:46
n = int(input())
inings = [list(map(int, input().split())) for _ in range(n)]

max_score = 0

# 게임플레이
def play(players):
    player_idx = 0
    score = 0
    for ining in inings:
        out_count = 0
        b1, b2, b3 = 0, 0, 0
        while out_count < 3:
            if ining[players[player_idx]] == 0:
                out_count += 1
            elif ining[players[player_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif ining[players[player_idx]] == 2:
                score += (b3 + b2)
                b1, b2, b3 = 0, 1, b1
            elif ining[players[player_idx]] == 3:
                score += (b3 + b2 + b1)
                b1, b2, b3 = 0, 0, 1
            elif ining[players[player_idx]] == 4:
                score += (b3 + b2 + b1 + 1)
                b1, b2, b3 = 0, 0, 0 
            player_idx = (player_idx + 1) % 9
    return score

# 타자 순서 (순열)
for players in permutations(range(1, 9), 8):
    players = list(players)
    players = players[:3] + [0] + players[3:]
    max_score = max(max_score, play(players))

print(max_score)