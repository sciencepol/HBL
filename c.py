import random


players = []

def generate_name():
    return(chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122)))

def add_player(name,score):
#    name = input("What is your name: ")
#    score = input("What is your score? : ")
    players.append([name,score])
    
for i in range(5000):
    add_player(generate_name(),random.randint(0,9999))
