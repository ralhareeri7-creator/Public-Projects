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
    "    -----------------"
)

#------- states------
"INIT"
"GREEN"
"GREEN_WAIT"
"YELLOW"
"RED"
"FLASH_YELLOW"
"SINK"

# use these strings in your input and print statements.
":~Enter a sequence (t,e,p,r,w). Empty line = quit ~:"
"Error: sequence must be at least 3 characters.\n"
"You entered: {}"
"Invalid sequence -- ended in SINK.\n"
"Valid sequence -- final state: {}\n"
"Goodbye!"

def red_transition(ch, red_timer):
    """
    Handles transitions while current state is RED.
    Returns ONLY the next state (timer is updated by the caller).

    """
    if ch == 't':
        if red_timer > 1:
            return "RED"
        else:
            # red_timer == 1 -> leave RED to GREEN
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
       value is user input in str1 and fsm is start of value set to INIT
       then it goes to the other colors
       """
    value = state
    fsm_state = "INIT"

    if value == "":
        return ""
    if len(value) < 3:
        return "ERRmsg"

    print(f"You entered: {value}")

    """
    RED timer setup
    """
    cross_ticks = 3
    red_timer = 0

    i = 0
    while i < len(value):
        ch = value[i]

        if ch != 't' and ch != 'e' and ch != 'p' and ch != 'r' and ch != 'w':
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
            if ch == 't' or ch == 'p' or ch == 'w':
                fsm_state = "FLASH_YELLOW"
            elif ch == 'r' or ch == 'e':
                fsm_state = "RED"

        elif fsm_state == "RED":

            if ch == 't':

                if red_timer > 1:
                    fsm_state = "RED"
                    red_timer = red_timer - 1
                else:
                    fsm_state = "GREEN"
                    red_timer = 0
            elif ch == 'e':
                fsm_state = "RED"
                red_timer = cross_ticks
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"
                red_timer = 0
            elif ch == 'w':
                fsm_state = "RED"
        else:
            fsm_state = "SINK"

        if prev_state != "RED" and fsm_state == "RED":
            red_timer = cross_ticks

        if fsm_state == "SINK":
            return "SINK"

        i = i + 1

    return fsm_state

def main():
    print(BANNER)
    str1 = input(":~Enter a sequence (t,e,p,r,w). Empty line = quit ~:").lower()
    while str1 != "":
        result = start(str1)
        if result == "ERRmsg":
            print("Error: sequence must be at least 3 characters.\n")
        elif result == "SINK":
            print("Invalid sequence -- ended in SINK.\n")
            break
        else:
            print(f"Valid sequence -- final state: {result}\n")
        str1 = input(":~Enter a sequence (t,e,p,r,w). Empty line = quit ~:").lower()

    if str1 == "":
        print("Goodbye!")


# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
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



def start(sequence):
    """
    Process one input sequence through the FSM.

    Grader requirements implemented:
      • Start from 'INIT' for the first sequence only.
      • For all following sequences, continue from the state (and RED timer) where we left off.

    Returns:
      ""        -> if empty input (caller exits)
      "ERRmsg"  -> if sequence length < 3
      "SINK"    -> if invalid input or fall into sink
      <STATE>   -> final state string of this sequence
    """
    # --- Lazy-init persistent attributes on the function itself ---
    if not hasattr(start, "_initialized"):
        start.fsm_state = "INIT"     # persistent FSM state
        start.red_timer = 0          # persistent RED timer
        start.first_sequence = True  # only the very first processed sequence starts from INIT
        start._initialized = True

    value = sequence

    # Quit case
    if value == "":
        return ""

    # Minimum length rule (keep original behavior)
    if len(value) < 3:
        # Mark that we've consumed the first attempt (we still continue from current state next time)
        start.first_sequence = False
        print(f"You entered: {value}")
        return "ERRmsg"

    print(f"You entered: {value}")

    # --- Setup initial state for this run ---
    if start.first_sequence:
        fsm_state = "INIT"
        red_timer = 0
        start.first_sequence = False
    else:
        fsm_state = start.fsm_state
        red_timer = start.red_timer

    # RED timer config
    cross_ticks = 3  # When entering RED, load this many ticks

    i = 0
    while i < len(value):
        ch = value[i]

        # Validate input character
        if ch not in ('t', 'e', 'p', 'r', 'w'):
            # Persist the sink state and clear timer
            start.fsm_state = "SINK"
            start.red_timer = 0
            return "SINK"

        # Track previous state to detect RED entry and to update timer rules
        prev_state = fsm_state

        # --- FSM transitions ---
        if fsm_state == "INIT":
            if ch == 't':
                fsm_state = "GREEN"
            elif ch == 'e':
                fsm_state = "RED"
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"
            elif ch == 'w':
                fsm_state = "INIT"
            elif ch == 'r':
                # Keep benign: stay in INIT if reset pressed at INIT
                fsm_state = "INIT"

        elif fsm_state == "GREEN":
            if ch == 't':
                fsm_state = "YELLOW"
            elif ch == 'w':
                fsm_state = "GREEN_WAIT"
            elif ch == 'e':
                fsm_state = "RED"
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"
            elif ch == 'r':
                fsm_state = "SINK"

        elif fsm_state == "GREEN_WAIT":
            if ch == 't':
                fsm_state = "YELLOW"
            elif ch == 'w':
                fsm_state = "GREEN_WAIT"
            elif ch == 'e':
                fsm_state = "RED"
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"
            elif ch == 'r':
                fsm_state = "SINK"

        elif fsm_state == "YELLOW":
            if ch == 't' or ch == 'e':
                fsm_state = "RED"
            elif ch == 'p':
                fsm_state = "FLASH_YELLOW"
            elif ch == 'w':
                fsm_state = "YELLOW"
            elif ch == 'r':
                fsm_state = "SINK"

        elif fsm_state == "FLASH_YELLOW":
            if ch in ('t', 'p', 'w'):
                fsm_state = "FLASH_YELLOW"
            elif ch in ('r', 'e'):
                fsm_state = "RED"
            else:
                fsm_state = "SINK"

        elif fsm_state == "RED":
            fsm_state = red_transition(ch, red_timer)

        else:
            fsm_state = "SINK"

        # --- Timer management: set timer on entry to RED ---
        if prev_state != "RED" and fsm_state == "RED":
            red_timer = cross_ticks

        # --- Timer updates while we are leaving/being in RED ---
        if prev_state == "RED":
            if ch == 't':
                if fsm_state == "RED":
                    red_timer -= 1
                elif fsm_state == "GREEN":
                    red_timer = 0
            elif ch == 'e':
                red_timer = cross_ticks
            elif ch == 'p':
                red_timer = 0
            elif ch == 'w':
                pass  # wait does not change red_timer while staying RED

        if fsm_state == "SINK":
            # Persist sink result
            start.fsm_state = "SINK"
            start.red_timer = 0
            return "SINK"

        i += 1

    # --- Persist final state and timer for next sequence ---
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