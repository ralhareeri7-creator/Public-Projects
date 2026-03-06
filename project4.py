################################################################################
#
# Computer Project 04
#   Description:
#   This program is mathematical model game called finite-state machine (FSM)
#
#   The script performs the following tasks:
#   1)user inputs a squence of letters such as t,e,p,r,w
#   2)program returns the state user is in and reprompts until
#     user types quit, empty quote, or an invalid
#     sequence of characters
#   3) Program handles a basic cycle INIT,Green,Yellow,and Red.
#      Once it is working, timer starts from red=3, -1, and
#      Moves to Green
#
#
#
#
#
#
#
#
################################################################################


# --- BANNER (read-only global variable allowed) ---
BANNER = (
    "    TRAFFIC LIGHT FSM\n"
    "    ------------------\n"
    "        +-----------+\n"
    "        |   [RED]   |\n"
    "        | [YELLOW]  |\n"
    "        |  [GREEN]  |\n"
    "        +-----------+\n"
    "    Pedestrian Button + Timer\n"
    "    -----------------\n"
)


def get_value():
    """
    Function is responsible for user input.
    It is called in the main and stored through a variable called prompt

    """
    str1 = input(":~Enter a sequence (t,e,p,r,w). Empty line = quit ~:").lower()
    return str1


def red_transition(ch, red_timer):
    """
    Handles transitions while current state is RED.
    Returns ONLY the next state (timer is updated by the caller).

    """
    if ch == 't':
        if red_timer > 1:
            return "RED"
        else:
            return "GREEN"
    elif ch == 'e':
        return "RED"
    elif ch == 'p':
        return "FLASH_YELLOW"
    elif ch == 'w':
        return "RED"
    else:
        return "SINK"


def start(state):
    """
    value is user input in prompt and FSM is start of value set to INIT
    then it goes to the other colors
       """

    if not hasattr(start, "_initialized"):
        """
        checks whether the function already has an _initialized attribute

        """
        start.fsm_state = "INIT"
        start.red_timer = 0
        start.first_state = True
        start._initialized = True

    value = state

    if value == "":
        return ""
    if len(value) < 3:
        start.first_state = False
        return "ERRmsg"

    print(f"You entered: {value}")

    if start.first_state:
        fsm_state = "INIT"
        red_timer = 0
        start.first_state = False
    else:
        fsm_state = start.fsm_state
        red_timer = start.red_timer

    """
    RED timer setup
    """
    cross_ticks = 3

    i = 0
    while i < len(value):
        ch = value[i]

        if ch not in ('t', 'e', 'p', 'r', 'w'):
            start.fsm_state = "SINK"
            start.red_timer = 0
            return "SINK"

        """
        Save previous state to detect entry into RED
        """
        prev_state = fsm_state

        if fsm_state == "INIT":
            if ch == 't':
                fsm_state = "GREEN"
            elif ch == 'e':
                fsm_state = "RED"
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"
            elif ch == 'w':
                fsm_state = "INIT"
            else:
                fsm_state = "SINK"

        elif fsm_state == "GREEN":
            if ch == 't':
                fsm_state = "YELLOW"
            elif ch == 'w':
                fsm_state = "GREEN_WAIT"
            elif ch == 'e':
                fsm_state = "RED"
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"


        elif fsm_state == "GREEN_WAIT":
            if ch == 't':
                fsm_state = "YELLOW"
            elif ch == 'w':
                fsm_state = "GREEN_WAIT"
            elif ch == 'e':
                fsm_state = "RED"
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"


        elif fsm_state == "YELLOW":
            if ch == 't' or ch == 'e':
                fsm_state = "RED"
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"
            elif ch == 'w':
                fsm_state = "YELLOW"

        elif fsm_state == "FLASH_YELLOW":
            if ch in ('t', 'p', 'w'):
                fsm_state = "FLASH_YELLOW"
            elif ch in ('r', 'e'):
                fsm_state = "RED"

        elif fsm_state == "RED":
            fsm_state = red_transition(ch, red_timer)

        else:
            fsm_state = "SINK"

        if prev_state != "RED" and fsm_state == "RED":
            red_timer = cross_ticks

        if prev_state == "RED":
            if ch == 't':
                if fsm_state == "RED":
                    red_timer = red_timer - 1
                elif fsm_state == "GREEN":
                    red_timer = 0
            elif ch == 'e':
                red_timer = cross_ticks
            elif ch == 'p':
                red_timer = 0
            elif ch == 'w':
                pass

        if fsm_state == "SINK":
            start.fsm_state = "SINK"
            start.red_timer = 0
            return "SINK"

        i += 1

    start.fsm_state = fsm_state
    start.red_timer = red_timer

    return fsm_state


def main():
    print(BANNER)
    prompt = get_value()
    while prompt != "":
        result = start(prompt)
        if result == "ERRmsg":
            print("Error: sequence must be at least 3 characters.\n")
        elif result == "SINK":
            print("Invalid sequence -- ended in SINK.\n")
            break
        else:
            print(f"Valid sequence -- final state: {result}\n")
        prompt = get_value()

    if prompt == "":
        print("Goodbye!")


# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
