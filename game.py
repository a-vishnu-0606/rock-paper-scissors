import random
choices = ["Stone", "Paper", "Scissors"]
system_score = 0
player_score = 0
while True:
    player = input("Stone, Paper or  Scissors?").capitalize()
    system = random.choice(choices)
    if player == system:
        print("Tie!")
    elif player == "Stone":
        if system == "Paper":
            print("You lose!", system, "covers", player)
            system_score = system_score+1
        else:
            print("You win!", player, "smashes", system)
            player_score = player_score+1
    elif player == "Paper":
        if system == "Scissors":
            print("You lose!", system, "cut", player)
            system_score = system_score+1
        else:
            print("You win!", player, "covers", system)
            player_score = player_score+1
    elif player == "Scissors":
        if system == "Stone":
            print("You lose!", system, "smashes", player)
            system_score = system_score+1
        else:
            print("You win!", player, "cut", system)
            player_score = player_score+1
    elif player=='End':
        print("Final Scores:")
        print("system score:",system_score)
        print("Player:",player_score)
        break




