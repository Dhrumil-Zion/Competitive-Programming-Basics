testcase = int(input())
play1_score = 0
play2_score = 0
maxx = 0
for _ in range(testcase):
    score1,score2 = map(int, input().split())
    play1_score += score1
    play2_score += score2
    diff = play1_score - play2_score
    if diff > maxx:
        winner = 1
        maxx = diff
    elif abs(diff) > maxx:
        winner = 2
        maxx = abs(diff)
print(winner, maxx)
