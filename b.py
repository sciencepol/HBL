
def sort_players():
    eff = len(players)
    swapped = True
    while swapped:
        swapped = False
        for k in range(0,eff-1):
            if players[k][1]>players[k+1][1]:
                players[k],players[k+1]=players[k+1],players[k]
                swapped = True
        eff-=1
