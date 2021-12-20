import random

rock_paper_scissors_v1 = ["rock","paper","scissors"]
rock_paper_scissors_v2 = ["rock","gun","lightning","devil","dragon","water","air","paper","sponge","wolf","tree","human","snake","scissors","fire"]
player2_or_computer = " "
computer_or_human = 0


def rock_paper_scissorcs_v1(computer_or_human):
    while True:

        player = input("rock,paper or scissors?:")
        if computer_or_human == 1:
            player2_or_computer = random.choice(rock_paper_scissors_v1)

        elif computer_or_human == 2:
            player2_or_computer = input("rock, paper, or scissors?:")

            while player2_or_computer not in rock_paper_scissors_v1:
                player2_or_computer = input("rock, paper, or scissors?: ")

        if player == player2_or_computer:
                print("Tie!")


                if player == rock_paper_scissors_v1[0]:
                    if player2_or_computer == rock_paper_scissors_v1[1]:
                        print("=============================")
                        print("Win Computer")
                        print("Computer choices: " + player2_or_computer)
                        print("You choices: " + player)
                        print("=============================")

                    elif player2_or_computer == rock_paper_scissors_v1[2]:
                        print("=============================")
                        print("Win Player")
                        print("Computer choices: " + player2_or_computer)
                        print("You choices: " + player)
                        print("=============================")

                elif player == rock_paper_scissors_v1[1]:
                    if player2_or_computer == rock_paper_scissors_v1[0]:
                        print("=============================")
                        print("Win Player")
                        print("Computer choices: " + player2_or_computer)
                        print("You choices: " + player)
                        print("=============================")

                    elif player2_or_computer == rock_paper_scissors_v1[2]:
                        print("=============================")
                        print("Win Computer")
                        print("Computer choices: " + player2_or_computer)
                        print("You choices: " + player)
                        print("=============================")


                elif player == rock_paper_scissors_v1[2]:
                    if player2_or_computer == rock_paper_scissors_v1[0]:
                        print("=============================")
                        print("Win Computer")
                        print("Computer choice: " + player2_or_computer)
                        print("You choice: " + player)
                        print("=============================")

                    elif player2_or_computer == rock_paper_scissors_v1[1]:
                        print("=============================")
                        print("Win Player")
                        print("Computer choice: " + player2_or_computer)
                        print("You choice: " + player)
                        print("=============================")

            play_again = input("Play again? (yes/no): ").lower()
            print("**********************************************")

            if play_again != "yes":
                break
                print("See you again.")



rock_paper_scissorcs_v1()



