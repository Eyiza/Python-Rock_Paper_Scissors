import random
print("Welcome to a game of Rock, Paper, Scissors")
print("Tip:\n Rock beats Scissors \n Paper beats Rock \n Scissors beats Paper")
print("R represents Rock, P represents Paper, and S represents Scissors")
print('Pick a choice: "R", "P" or "S" ')

while True:
    player_choice = input("Choice: ").upper()
    CPU_choice = ['P', 'R', 'S']

    while player_choice not in CPU_choice:
        print("Invalid input")
        player_choice = input("Enter a valid input (P, R or S): ").upper()

    CPU = random.choice(CPU_choice)
    print("CPU's choice is {}".format(CPU))

    print("{} vs {}".format(player_choice, CPU))

    if CPU == player_choice:
        print("It's a tie")
    elif CPU == 'R' and player_choice == 'P':
        print("You win! Paper beats Rock")
    elif CPU == 'P' and player_choice == 'S':
        print("You win! Scissors beats Paper")
    elif CPU == 'S' and player_choice == 'R':
        print("You win! Rock beats Scissors")
    elif CPU == 'P' and player_choice == 'R':
        print("You lose! Paper beats Rock")
    elif CPU == 'S' and player_choice == 'P':
        print("You lose! Scissors beats Paper")
    elif CPU == 'R' and player_choice == 'S':
        print("You lose! Rock beats Scissors")


    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break