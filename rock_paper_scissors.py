import random

rock_paper_scissors_v1 = ["rock","paper","scissors"]
rock_paper_scissors_v2 = ["rock","gun","lightning","devil","dragon","water","air","paper","sponge","wolf","tree","human","snake","scissors","fire"]

print("****************************************************")
print("                Rock, Paper,Scissors                ")
print("V1 = rock, paper and scissors")
print("V2 = rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors and fire")
print("****************************************************")
v1_or_v2 = input("     V1 or V2 :").lower()



if v1_or_v2 == "v1":

    while True:
        print("---------------------------------------------------")
        print("Player1 Choice")
        player = input("rock,paper or scissors? :")
        print("---------------------------------------------------")

        while player not in rock_paper_scissors_v1:
            print("---------------------------------------------------")
            print("Please choose between rock, paper and scissors.")
            print("Player1 Choice")
            player = input("rock,paper or scissors?")
            print("---------------------------------------------------")

        computer = random.choice(rock_paper_scissors_v1)

        if player == computer:
            print("---------------------------------------------------")
            print("                       Tie!                        ")
            print("---------------------------------------------------")

        elif player == rock_paper_scissors_v1[0]:
            if computer == rock_paper_scissors_v1[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + rock_paper_scissors_v1[1])
                print("Player choice: " + rock_paper_scissors_v1[0])
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v1[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + rock_paper_scissors_v1[2])
                print("Player choice:" + rock_paper_scissors_v1[0])
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v1[1]:
            if computer == rock_paper_scissors_v1[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + rock_paper_scissors_v1[0])
                print("Player choice: " + rock_paper_scissors_v1[1])
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v1[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + rock_paper_scissors_v1[2])
                print("Player choice: " + rock_paper_scissors_v1[1])
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v1[2]:
            if computer == rock_paper_scissors_v1[0]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + rock_paper_scissors_v1[0])
                print("Player choice: " + rock_paper_scissors_v1[2])
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v1[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + rock_paper_scissors_v1[1])
                print("Player choice: " + rock_paper_scissors_v1[2])
                print("---------------------------------------------------")


        print("Play again?")
        play_again = input("     Yes or No :").lower()

        if play_again != "yes":
            print("See you again.")
            break




elif v1_or_v2 == "v2":
    while True:
        print("---------------------------------------------------")
        print("Player1 Choice")
        player = input("rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors, fire? :")
        print("---------------------------------------------------")

        while player not in rock_paper_scissors_v2:
            print("---------------------------------------------------")
            print("Please choose between rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors and fire.")
            print("Player1 Choice")
            player = input("rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors and fire?")
            print("---------------------------------------------------")

        computer = random.choice(rock_paper_scissors_v2)

        if player == computer:
            print("---------------------------------------------------")
            print("                       Tie!                        ")
            print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[0]:

