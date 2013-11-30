import random

def add_player():
    name = input("What is your name: ")
    score = input("What is your score? : ")
    players.append([name,score])
    
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


def generate_name():
    return(chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122)))


def binary_search(elements, target, low, high):
  mid = (low + high) // 2
  if low > high: 
    return high + 1
  elif elements[mid][1] == target:
    return mid + 1
  elif target < elements[mid][1]: 
    return binary_search(elements, target, low, mid-1)
  else: 
    return binary_search(elements, target, mid+1, high)


def find_player(name):
    for i in players:
        if i[0] == name:
            print(i)
            break

def same_score():
    same_score=[]
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
    return(same_score)

def close_score(player_score):
    number = binary_search(players,player_score,0,len(players)-1)
    for i in range(number-5, number):
        print (players[i])
    for i in range(number+1, number+6):
        print (players[i])

players = []

def display():
    while True:
        print('Welcome')
        print('A: Add your name and score')
        print('B: Generate a random name and score')
        print('C: View leaderboard')
        print('D: Look for your score')
        print('E: Find players with the same score')
        print('F: See who is above/below you')
        print('G: Quit')
        choice = input('Choose')
        if choice == 'A':
            add_player()
        elif choice == 'B':
            players.append([generate_name(),random.randint(0,9999)])
        elif choice == 'C':
            sort_players()
            print("The top player is ", players[-1][0])
        elif choice == 'D':
            score = input("What is your name")
            find_player(score)
        elif choice == 'E':
            print(same_score())
        elif choice == 'F':
            player_score = input("What is your score")
            close_score(player_score)
        elif choice == 'G':
            print('Thanks for playing!')
            break
        

    
