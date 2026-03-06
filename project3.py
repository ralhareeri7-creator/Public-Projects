################################################################################
#
# Computer Project 03
#   Description:
#   This program is a designed to improve and analyze DNA sequence alignment
#
#   The script performs the following tasks:
#   1) user will choose a prompt from the menu
#   2) program will either preform DNA Squence Alignment,
#      display menu options again, or exist game.
#   3) if user chooses DNA Squence Alignment, user will be provided
#       with two strings to type the DNA, The strings do not have to be
#       same length.
#
#   4) action variable will be displaced asking user to either
#       add or delete indel, score, or quit the game.
#   5) if user selects score, program will
#       report the number of matches and the number of mismatches
#   6)Matching characters even if upper case, will be printed
#       in lower case
#   7)All mismatches are printed in upper case.
#       Indels are printed as dashes.
#
#
#
#
################################################################################


BANNER = (
    "============================================\n"
    "    PROJECT HELIX: DNA ALIGNMENT\n"
    "============================================\n"
    "    Optimizing DNA Storage & Transmission\n"
    "    Accelerating Bioinformatics Research\n"
    "\n"
    "    A--T   C--G   G--C   T--A   A--T   G--C\n"
    "    |      |      |      |      |      |\n"
    "    T--A   G--C   C--G   A--T   T--A   C--G\n"
    "============================================"
)

MENU = (
    "\nPlease choose one of the options below:\n"
    "  A. DNA Sequence Alignment\n"
    "  H. Display the menu of options.\n"
    "  X. Exit."
)

ACTION = (
    "\n:~What do you want to do:\n"
    "  a (add indel)\n"
    "  d (delete indel)\n"
    "  s (score)\n"
    "  q (quit) ~:"
)

# Constant of allowed characters
DNA_LETTERS = "ATCGatcg"

# Print the initial banner and menu to the user
print(BANNER)
print(MENU)

while True:
    question1 = input("\n:~Enter option ~:").lower()

    if question1 == "a":

        while True:
            s1 = input("\n:~Input String 1 ~:")
            count = 0
            for ch in s1:
                if ch.lower() not in DNA_LETTERS:
                    count += 1
                    break
            if s1 == "" or count != 0:
                print("Invalid characters in the DNA sequence\n")
            else:
                break

        while True:
            s2 = input(":~Input String 2 ~:")
            count = 0
            for ch in s2:
                if ch.lower() not in DNA_LETTERS:
                    count += 1
                    break
            if s2 == "" or count != 0:
                print("Invalid characters in the DNA sequence\n")
            else:
                break

        while True:
            option = input(ACTION).lower()

            if option == "a":
                sn = int(input("\n:~Work on which string (1 or 2) ~:"))
                insert_index = int(input(":~Before what index ~:"))

                if sn == 1:
                    while insert_index >= len(s1):
                        print("Insert index out of range\n")
                        insert_index = int(input(":~Before what index ~:"))
                    s1 = s1[:insert_index] + "-" + s1[insert_index:]

                elif sn == 2:
                    while insert_index >= len(s2):
                        print("Insert index out of range\n")
                        insert_index = int(input(":~Before what index ~:"))
                    s2 = s2[:insert_index] + "-" + s2[insert_index:]

            elif option == "d":
                sn = int(input("\n:~Work on which string (1 or 2) ~:"))
                delete_index = int(input(":~Delete what  ~:"))

                if sn == 1:
                    if delete_index >= len(s1):
                        print("Delete index out of range\n")
                    elif s1[delete_index] != "-":
                        print("Not an indel")
                    else:
                        s1 = s1[:delete_index] + s1[delete_index + 1:]

                elif sn == 2:
                    if delete_index >= len(s2):
                        print("Delete index out of range\n")
                    elif s2[delete_index] != "-":
                        print("Not an indel")
                    else:
                        s2 = s2[:delete_index] + s2[delete_index + 1:]






            elif option == "s":
                l = min(len(s1), len(s2))
                matches = 0
                missmatches = 0

                disp1 = ""
                disp2 = ""

                for i in range(l):
                    if s1[i] != "-" and s2[i] != "-":
                        if s1[i] == s2[i]:
                            matches += 1
                            disp1 += s1[i].lower()
                            disp2 += s2[i].lower()
                        else:
                            missmatches += 1
                            disp1 += s1[i].upper()
                            disp2 += s2[i].upper()

                    else:
                        # Handle indels properly
                        if s1[i] == "-" and s2[i] == "-":
                            missmatches += 1
                            disp1 += "-"
                            disp2 += "-"
                        elif s1[i] == "-":
                            missmatches += 1
                            disp1 += "-"
                            disp2 += s2[i].upper()
                        elif s2[i] == "-":
                            missmatches += 1
                            disp1 += s1[i].upper()
                            disp2 += "-"

                if len(s1) > l:
                    missmatches += len(s1) - l
                    disp1 += s1[l:].upper()
                    disp2 += "-" * (len(s1) - l)

                elif len(s2) > l:
                    missmatches += len(s2) - l
                    disp2 += s2[l:].upper()
                    disp1 += "-" * (len(s2) - l)

                print(f"\nMatches: {matches} Mismatches: {missmatches}")
                print(f"String 1: {disp1}")
                print(f"String 2: {disp2}")

            elif option == "q":
                break

    elif question1 == "h":
        print(MENU)

    elif question1 == "x":
        print("Exiting program...\nBeware of computational biologist they screw genes and protein!")
        break

    else:
        print("Invalid options. Please try again")