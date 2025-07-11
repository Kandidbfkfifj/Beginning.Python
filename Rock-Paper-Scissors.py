#Rock-paper-scissors.py
import random 
def player_choice(): #defining the players choice function
    choice = input("Choose rock, paper, or scissors: ")
    choice = choice.lower()
    if choice == "rock":
        print("You choose Rock.")
    elif choice == "paper":
        print("You choose paper.")
    elif choice == "scissors":
        print("You choose scissors.")
    else:
        print("invalid choice,try again please.")
        return player_choice()
    return choice
def cpu_choice(): #defining the cpus random choice function
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(player, cpu):  #setting the rules of the game and determing the winner
    if player == cpu:
     return "it's a tie so it is undecided, good luck next time:)"
    elif (player == "rock" and cpu == "paper"):
        print("You lose!:), paper covers rock")
        return "CPU wins!"
    elif (player == "paper" and cpu == "rock"):
        print("You win!;), paper covers rock")
        return "Player wins!"
    elif (player == "scissors" and cpu == "rock"):
        print("You lose :(, scissors get crushed by rock")
        return "CPU wins!"
    elif (player == "rock" and cpu == "scissors"):
        print("You win! ;), Rock crushes scissors")
        return "Player wins!"
    elif (player == "scissors" and cpu == "paper"):
        print("You win! ;), scissors cut paper")
        return "Player wins!"
    elif (player == "paper" and cpu == "scissors"):
        print("You lose :(, paper gets cut by scissors")
        return "CPU wins!"
def play_game():  #main function to start and play the game 
        player = player_choice()
        cpu = cpu_choice()
        print(f"CPU choose {cpu}")
        return determine_winner(player, cpu)
if __name__ == "__main__":
        while True:  #loop to keep the game running till the player decides to stop
            result = play_game()
            print(result)
            if result == "CPU wins!":
                print("Better luck next time!")
            elif result == "Player wins!":
                print("Congrats!, you won!")
            elif "tie" in result.lower():
                print("It is a tie, try again pls.")
#is there maybe a way for me to mak the game more attractive and expand it more?
#i know we have not had the chance to learn abt the return function or the topic "functions"
#but before i started learning pathon at codex i was learning it from a different website and
#thats why i know abt the functions and how to use them