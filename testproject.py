
# ask to play
str1 = int(input("\n:~Would you like to play? (0=no, 1=yes) ~: "))

# simple cumulative record (needed for the end-of-game messages)
human_wins = 0
comp_wins = 0
games_played = 0

# single main loop
while str1 != 0:
    print("\nStarting a new game...")

    # keep asking for total stones until it's odd and > 1
    str2 = int(input("\n:~How many stones would you like to play? ~: "))
    while str2 <= 1 or str2 % 2 == 0:
        print("The total number of stones must be odd and greater than 1.")
        str2 = int(input("\n:~How many stones would you like to play? ~: "))

    # valid: proceed with the rest of the game here
    pile1 = (str2 + 1) // 2   # larger half (e.g., 9 -> 5)
    pile2 = str2 // 2         # smaller half (e.g., 9 -> 4)
    print(f"Start --> Pile 1: {pile1}, Pile 2: {pile2}")

    # per-game tallies (to determine odd/even winner)
    human_score = 0
    comp_score = 0

    # play one full game until no stones remain
    while pile1 > 0 or pile2 > 0:
        # --- Human: choose a pile (must be 1 or 2 AND non-empty) ---
        str3 = int(input("\n:~Choose a pile (1 or 2) ~: "))
        while (str3 != 1 and str3 != 2) or (str3 == 1 and pile1 == 0) or (str3 == 2 and pile2 == 0):
            print("Pile must be 1 or 2 and non-empty. Please try again.")
            str3 = int(input("\n:~Choose a pile (1 or 2) ~: "))

        # --- Human: choose stones to remove (1–3 and not more than the chosen pile) ---
        str4 = int(input(":~Choose stones to remove from pile ~: "))
        max_allowed = pile1 if str3 == 1 else pile2
        while str4 < 1 or str4 > 3 or str4 > max_allowed:
            if str4 < 1 or str4 > 3:
                print("You must remove 1, 2, or 3 stones. Please try again.")
            else:
                print("You cannot remove more stones than the pile holds. Please try again.")
            str4 = int(input(":~Choose stones to remove from pile ~: "))

        # apply human move
        if str3 == 1:
            pile1 -= str4
        else:
            pile2 -= str4
        human_score += str4
        print(f"You removed {str4} from Pile {str3}. Pile 1 = {pile1}, Pile 2 = {pile2}")

        # if both piles empty after human, game ends before computer acts
        if pile1 == 0 and pile2 == 0:
            break

        # --- Computer move: chooses the other pile; if empty, uses the same; removes exactly 1 ---
        if str3 == 1:
            # human used pile 1, computer tries pile 2
            if pile2 > 0:
                pile2 -= 1
                comp_score += 1
                print(f"Computer removes 1 from Pile 2. Pile 1 = {pile1}, Pile 2 = {pile2}")
            elif pile1 > 0:
                pile1 -= 1
                comp_score += 1
                print(f"Computer removes 1 from Pile 1. Pile 1 = {pile1}, Pile 2 = {pile2}")
        else:
            # human used pile 2, computer tries pile 1
            if pile1 > 0:
                pile1 -= 1
                comp_score += 1
                print(f"Computer removes 1 from Pile 1. Pile 1 = {pile1}, Pile 2 = {pile2}")
            elif pile2 > 0:
                pile2 -= 1
                comp_score += 1
                print(f"Computer removes 1 from Pile 2. Pile 1 = {pile1}, Pile 2 = {pile2}")

        # loop continues until both piles are empty

    # --- Game over: decide winner by odd number of stones collected ---
    games_played += 1
    if human_score % 2 == 1:
        human_wins += 1
        print("\nYou win! You ended with an odd number of stones.")
    else:
        comp_wins += 1
        print("\nComputer wins! Computer ended with an odd number of stones.")

    # show record and ask to play again (do not reprint banner/rules here)
    print(f"\nRecord: You {human_wins} – Computer {comp_wins}  (Games: {games_played})")
    str1 = int(input("\n:~Would you like to play again? (0=no, 1=yes) ~: "))

print("\nThanks for playing! See you again soon!")
