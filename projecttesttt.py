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


#problems with code: string1 keeps repeating preveting other code
#from excuting such as action bar fetaures,score,quit,indels
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
    question1= input("\n:~Enter option ~:").lower()
    #starting alignment and vaildating string 1
    if question1 == "x":
        print ("existing")
        break
    if question1=="a":

        while True:
            str1 = input("\n:~Input String 1 ~:")
            count =0
            for ch in str1:
                if ch.lower() not in DNA_LETTERS:
                    count+=1
                    break
            if str1 != "" or count !=0:
                print("Invalid characters in the DNA sequence\n")
            else:
                break

        while True:
            str2 = input(":~Input String 2 ~:")
            count = 0
            for ch in str2:
                if ch.lower() not in DNA_LETTERS:
                    count += 1
                    break
            if str2 != "" or count != 0:
                print("Invalid characters in the DNA sequence\n")
            else:
                break


    while True:
        option = option = input(ACTION).lower()
        if option =="a":
            if sn == 1:
                while insert_index >= len(str_one):
                    print("insert index of range")
                    delete_index=
            for ch in str1:
                if ch.lower() not in DNA_LETTERS:
                    count+=1
                    break
                if str1=="" or count !=0
                    print ("invaild")

            if sn == 2:
            sn=input("work on which string")

            insert_index = int(input(":before what index")
        if option =="d":
            sn = int(input("work on which string 1 or 2"))
            delete_index = input(":Delete what")
            if sn==1:
                while delete_index>=len(s1)
                    print("delete index of range")
                    delet_index


            if sn==2:


        if option =="s":
            1=min(len(s1), len (s2)))
            matches=0
            missmatch=0
            for i in range (1):
                if str1[i] != "-" and str2[i]!="-":
                    if str1[i]==str2[i]:
                        matches+=1
                    else:
                        missmatch+=1
        else:
            missmatches+=1
    missmatches+=max(len(str1), len(str2)-min(len(str1), len(str2))
    print("matches {matches}   ", Matches, {mismatches} ")
    print (f"string 1: {str1}"
           (f"string (str2)





         if option!="q":
            print ("message")
            break






    if question1 == "h":
        check1 = 0
            str1= input("\n:~Input String 1 ~:"))
            if len(str1) == 0:
                print("Invalid characters in the DNA sequence\n")
        else:
            i = 0
            invalid = 0
            while i < len(str1):
                ch = str1[i]
                okchar = 0
                k = 0
                while k < len(DNA_LETTERS):
                    if ch == DNA_LETTERS[k]:
                        okchar = 1
                        k = len(DNA_LETTERS)
                    else:
                        k = k + 1
                    if okchar == 0:
                        invalid1 = 1
                        i = len(str1)
                    else:
                        i = i + 1
                if invalid1 == 0:
                    check1 = 1
                else:
                    print("Invalid characters in the DNA sequence\n")


        #check for string 2
        check2 = 0
        while check2 == 0:
            str2 = str(input(":~Input String 2 ~:"))
            if len(str2) == 0:
                print("Invalid characters in the DNA sequence\n")
            else:
                j = 0
                invalid2 = 0
                while j < len(str2):
                    ch2 = str2[j]
                    okchar2 = 0
                    k2 = 0
                    while k2 < len(DNA_LETTERS):

                        if ch2 == DNA_LETTERS[k2]:
                            okchar2 = 1
                            k2 = len(DNA_LETTERS)
                        else:
                            k2 = k2 + 1
                    if okchar2 == 0:
                        invalid2 = 1
                        j = len(str2)
                    else:
                        j = j + 1
                    if invalid2 == 0:
                        check2 = 1
                    else:
                        print("Invalid characters in the DNA sequence\n")

        #ACTION loop
        running = 1
        while running == 1:
            print(ACTION)
            a = str(input())
            if a != '':
                a = a.lower()

                if a == 'a':
                    question2 = str(input("\n:~Work on which string (1 or 2) ~:"))
                    question3= str(input(":~Before what index ~:"))
                    ok = 1
                    if len(question3) == 0:
                        ok = 0
                    else:
                        index = 0
                        val = 0
                        while index < len(question3):
                            c = question3[index]
                            if c == '0': #c, current character
                                d = 0
                            elif c == '1':
                                d = 1
                            elif c == '2':
                                d = 2
                            elif c == '3':
                                d = 3
                            elif c == '4':
                                d = 4
                            elif c == '5':
                                d = 5
                            elif c == '6':
                                d = 6
                            elif c == '7':
                                d = 7
                            elif c == '8':
                                d = 8
                            elif c == '9':
                                d = 9
                        else:
                            ok = 0
                            index = len(question3)
                            d = 0
                        if ok == 1:
                            val = val * 10 + d
                            index = index + 1

                    if question2 == '1':
                        if ok == 1 and val >= 0 and val <= len(str1):
                            str1 = str1[0:val] + "-" + str1[val:len(str1)]
                        else:
                            print("Insert index out of range\n")
                    else:
                        if ok == 1 and val >= 0 and val <= len(str2):
                            str2 = str2[0:val] + "-" + str2[val:len(str2)]
                        else:
                            print("Insert index out of range\n")

                #delete indel

            elif a == 'd':
                targetd = str(input("\n:~Work on which string (1 or 2) ~:"))
                del_text = str(input(":~Delete what  ~:"))

                okd = 1
                if len(del_text) == 0:
                    okd = 0
                else:
                    q = 0
                    del_idx = 0
                    while q < len(del_text):
                        c2 = del_text[q]
                        if c2 == '0':
                            d2 = 0
                        elif c2 == '1':
                            d2 = 1
                        elif c2 == '2':
                            d2 = 2
                        elif c2 == '3':
                            d2 = 3
                        elif c2 == '4':
                            d2 = 4
                        elif c2 == '5':
                            d2 = 5
                        elif c2 == '6':
                            d2 = 6
                        elif c2 == '7':
                            d2 = 7
                        elif c2 == '8':
                            d2 = 8
                        elif c2 == '9':
                            d2 = 9
                        else:
                            okd = 0
                            q = len(del_text)
                            d2 = 0
                        if okd == 1:
                            del_idx = del_idx * 10 + d2
                            q = q + 1

                    if targetd == '1':
                        if okd == 1 and del_idx >= 0 and del_idx < len(str1):
                            if str1[del_idx] == '-':
                                str1 = str1[0:del_idx] + str1[del_idx + 1:len(str1)]
                            else:
                                print("Not an indel")
                        else:
                            print("Delete index out of range\n")
                    else:
                        if okd == 1 and del_idx >= 0 and del_idx < len(str2):
                            if str2[del_idx] == '-':
                                str2 = str2[0:del_idx] + str2[del_idx + 1:len(str2)]
                            else:
                                print("Not an indel")
                        else:
                            print("Delete index out of range\n")
            #score

            elif a == 's':
                L1 = len(str1)
                L2 = len(str2)
                L = L1
                if L2 > L:
                    L = L2
                i = 0
                out1 = ""
                out2 = ""
                matches = 0
                mismatches = 0
                while i < L:
                    if i < L1:
                        c1 = str1[i]
                    else:
                        c1 = '-'
                    if i < L2:
                        c2 = str2[i]
                    else:
                        c2 = '-'
                    if c1 == '-' or c2 == '-':
                        mismatches = mismatches + 1
                        if c1 == '-':
                            out1 = out1 + '-'
                        else:
                            out1 = out1 + c1.upper()
                        if c2 == '-':
                            out2 = out2 + '-'
                        else:
                            out2 = out2 + c2.upper()
                    else:
                        if c1.upper() == c2.upper():
                            matches = matches + 1
                            out1 = out1 + c1.lower()
                            out2 = out2 + c2.lower()
                        else:
                            mismatches = mismatches + 1
                            out1 = out1 + c1.upper()
                            out2 = out2 + c2.upper()
                    i = i + 1
                print("\nMatches: " + str(matches) + " Mismatches: " + str(mismatches))
                print("String 1: " + out1)
                print("String 2: " + out2)

                # Quit action loop
            elif a == 'q':
                running = 0

    #Prompt or next operation after quitting ACTION loop
        question1 = str(input("\n:~Enter option ~:"))

    elif question1.lower() == 'h' or question1.upper() == 'H':
        print(MENU)
        question1 = str(input("\n:~Enter option ~:"))

    elif question1.lower() == 'x' or question1.upper() == 'X':
        print("Exiting program...\nBeware of computational biologist they screw genes and protein!")
        break

    else:
        print("Invalid options. Please try again")
        print(MENU)
        question1 = str(input("\n:~Enter option ~:"))

print("Exiting program...\nBeware of computational biologist they screw genes and protein!")


"\n:~Enter option ~:"

"\n:~Input String 1 ~:"

":~Input String 2 ~:"

"Invalid characters in the DNA sequence\n"


"Insert index out of range\n"


"Insert index out of range\n"
":~Before what index ~:"

"\n:~Work on which string (1 or 2) ~:"



"Delete index out of range\n"
":~Delete what  ~:"
"Not an indel"





"\nMatches: {} Mismatches: {}"
"String 1: {}"
"String 2: {}"
"Invalid options. Please try again"


# Exit message when the user chooses to exit the program
"Exiting program...\nBeware of computational biologist they screw genes and protein!"
