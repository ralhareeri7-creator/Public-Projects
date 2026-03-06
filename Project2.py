################################################################################
#
# Computer Project 02
#
#   Description:
#   This program is a game called Oddly
#   It is a strategic mathematical game where the human and the computer
#   take turns playing by removing stones from two distinct piles.
#
#
#
#   The script performs the following tasks:
#   1) the human starts game
#   2)Then human answers a set of questions
#   3)human must choose one of the piles and remove either 1, 2, or 3 stones
#   4)the computer will select the pile that the player did not use on their turn
#   5) computer will always take 1 stone
#   6)The game continues until human or computer is unable
#    to make a move because there are no stones left to remove.
#
#
#
################################################################################


# Display the rules of the game
BANNER = """*** Welcome to the Oddly Game! ***
*Let's see if you can beat the odds!*"""

RULES = """\nOddly is a strategic two-player game that challenges your ability
to think ahead.
The game begins with two piles of stones split from an odd total number of stones.
Players take turns removing stones from the piles.
The game ends when all stones are removed. The winner? The player who ends up
with an odd number of stones!
Good luck, and don't let the computer outsmart you!"""

print(BANNER)
print(RULES)

# keeping track of score, stones, and games played
human_stone = 0
comp_stone = 0
human_score = 0
comp_score = 0

# variables
str1 = int(input("\n:~Would you like to play? (0=no, 1=yes) ~:"))

# loop for starting the game if user chooses 1
while str1 != 0:
    # generate questions
    print("\nStarting a new game...")

    # another loop to meet condition for total stones to be odd and > 1
    str2 = int(input("\n:~How many stones would you like to play? ~:"))
    while str2 <= 1 or str2 % 2 == 0:
        # checking for odd number of stones
        print("The total number of stones must be odd and greater than 1.")
        str2 = int(input("\n:~How many stones would you like to play? ~:"))

    # now total # of stones is split with pile1 being larger than pile2
    pile1 = (str2 + 1) // 2  # ex: if str2=5, 5+1/2=3
    pile2 = str2 // 2  # same here: 5//2=2

    # reset per-game counters
    human_stone = 0
    comp_stone = 0

    # displays stones
    print("Start --> Pile 1:", pile1, ", Pile 2:", pile2)
    while pile1 > 0 or pile2 > 0:
        str3 = int(input("\n:~Choose a pile (1 or 2) ~:"))
        while (str3 != 1 and str3 != 2) or (str3 == 1 and pile1 == 0) or (str3 == 2 and pile2 == 0):
            print("Pile must be 1 or 2 and non-empty. Please try again.")
            str3 = int(input("\n:~Choose a pile (1 or 2) ~:"))

        str4 = int(input("\n:~Choose stones to remove from pile ~:"))
        while (str4 < 1 or str4 > 3) or (str3 == 1 and str4 > pile1) or (str3 == 2 and str4 > pile2):

            if str4 < 1 or str4 > 3:
                print("Invalid number of stones. Please try again.")

            elif str3 == 1 and str4 > pile1:
                print("Invalid number of stones. Please try again.")
            elif str3 == 2 and str4 > pile2:
                print("Invalid number of stones. Please try again.")

            str4 = int(input("\n:~Choose stones to remove from pile ~:"))

        # human moves first
        if str3 == 1:
            pile1 -= str4
        else:
            pile2 -= str4
        human_stone += str4
        print("\nPlayer -> Remove", str4, "stones from pile", str3)
        print("Pile 1:", pile1, ", Pile 2:", pile2)
        # if both piles empty after human, game ends before computer acts
        if pile1 == 0 and pile2 == 0:
            break  # ends game, no code runs after

        if str3 == 1:
            # human used pile 1, computer tries pile 2
            if pile2 > 0:
                pile2 -= 1
                comp_stone += 1
                print("\nComputer -> Remove 1 stones from pile 2")
                print("Pile 1:", pile1, ", Pile 2:", pile2)
            elif pile1 > 0:
                pile1 -= 1
                comp_stone += 1
                print("\nComputer -> Remove 1 stones from pile 1")
                print("Pile 1:", pile1, ", Pile 2:", pile2)
        else:
            # human used pile 2, computer tries pile 1
            if pile1 > 0:
                pile1 -= 1
                comp_stone += 1
                print("\nComputer -> Remove 1 stones from pile 1")
                print("Pile 1:", pile1, ", Pile 2:", pile2)
            elif pile2 > 0:
                pile2 -= 1
                comp_stone += 1
                print("\nComputer -> Remove 1 stones from pile 2")
                print("Pile 1:", pile1, ", Pile 2:", pile2)

        # loop continues until both piles are empty
        # Game ends, decide winner by odd number of stones collected

    if human_stone % 2 == 1:
        human_score += 1
        print("\nStones -> human:", human_stone, "; computer:", comp_stone)
        print("CONGRATULATIONS! Player wins!")
    else:
        comp_score += 1
        print("\nStones -> human:", human_stone, "; computer:", comp_stone)
        print("Computer wins!")

    # show record and ask to play again (not showing banner/rules)
    print("\nCurrent Score -> human:", human_score, "; computer:", comp_score)
    str1 = int(input("\n:~Would you like to play again? (0=no, 1=yes) ~:"))

print("\nThanks for playing! See you again soon!")

# USE THE FOLLOWING IN YOUR INPUT STATEMENTS
"\n:~Would you like to play? (0=no, 1=yes) ~:"
"\n:~How many stones would you like to play? ~:"
"\n:~Choose a pile (1 or 2) ~:"
"\n:~Choose stones to remove from pile ~:"

# USE THE FOLLOWING IN YOUR PRINT STATEMENTS
"\nStarting a new game..."
"The total number of stones must be odd and greater than 1."
"Pile must be 1 or 2 and non-empty. Please try again."
"Invalid number of stones. Please try again."
"Computer wins!"
"CONGRATULATIONS! Player wins!"
"\nThanks for playing! See you again soon!"

# THE FOLLOWING SHOULD BE COMBINED INTO THE SAME PRINT STATEMENT

# Group 1
"Pile 1:"
", Pile 2:"

# Group 2
"\nStones -> human:"
"; computer:"

# Group 3
"\nCurrent Score -> human:"
"; computer:"

# Group 4
"Start --> Pile 1:"
", Pile 2:"

# Group 5
"\nPlayer -> "
"Remove"
"stones from pile"

# Group 6
"\nComputer -> "
"Remove"
"stones from pile"






