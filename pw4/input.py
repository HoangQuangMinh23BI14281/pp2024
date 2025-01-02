def get_input(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(f"{prompt}")
    stdscr.refresh()

    # Get the user input as a string
    user_input = ""
    while True:
        char = stdscr.getch()  # get a character
        if char == 10:  # Enter key is pressed
            break
        elif char == 27:  # Escape key (cancel)
            user_input = ""
            break
        elif char == 263:  # Backspace (delete last character)
            user_input = user_input[:-1]
        else:
            user_input += chr(char)  # Add the character to the input string

        # Display the current input in the window
        stdscr.clear()
        stdscr.addstr(f"{prompt}{user_input}")
        stdscr.refresh()

    return user_input
