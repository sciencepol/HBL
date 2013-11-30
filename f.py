same_score=[]
players=[['npv', 1111], ['liw', 1111], ['abw', 2461], ['tur', 1614], ['ziz', 4790]]
appended = False
for i in range(len(players)-1):
    if players[i][1] == players[i+1][1]:
        if appended:
            same_score.append(players[i+1])
        else:
            same_score.append(players[i+1])
            same_score.append(players[i])
            appended = True
    else:
        appended = False
