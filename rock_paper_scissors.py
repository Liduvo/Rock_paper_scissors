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
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v1[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice:" + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v1[1]:
            if computer == rock_paper_scissors_v1[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v1[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v1[2]:
            if computer == rock_paper_scissors_v1[0]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v1[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
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
        player = input("rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors, fire? :").lower()
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
            if computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2 [1]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[2]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[3]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[4]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")


            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[5]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[6]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[7]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")


            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[8]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")


            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[9]:
            if computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[10]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[11]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[12]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[13]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[14]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

        elif player == rock_paper_scissors_v2[14]:
            if computer == rock_paper_scissors_v2[0]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[1]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[2]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[3]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[4]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[5]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[6]:
                print("---------------------------------------------------")
                print("Computer Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[7]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[8]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[9]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[10]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[11]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[12]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")

            elif computer == rock_paper_scissors_v2[13]:
                print("---------------------------------------------------")
                print("Player Win!")
                print("Computer choice: " + computer)
                print("Player choice: " + player)
                print("---------------------------------------------------")


        print("Play again?")
        play_again = input("     Yes or No :").lower()

        if play_again != "yes":
            print("See you again.")
            break
