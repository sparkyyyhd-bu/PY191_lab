import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    # ==========================================================
    # INITIALIZE THE DISPLAY
    #
    # Display the document with the cursor at the current
    # cursor position.
    #
    # Example
    #
    # text    = "Hello"
    # cursor  = 0
    #
    # display = "|Hello"
    #
    # ---------------- TODO ----------------

    display = text[0:cursor] + "|" + text[cursor:]


    # ----------------------------------------

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor

    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break

        # ==========================================================
        # LEFT ARROW
        #
        # Move the cursor one position to the left.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 2
        # display = "He|llo"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_LEFT:

            if cursor > 0:
                cursor -= 1


        # ----------------------------------------

        # ==========================================================
        # RIGHT ARROW
        #
        # Move the cursor one position to the right.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 4
        # display = "Hell|o"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_RIGHT:

            if cursor < len(text):
                cursor += 1



        # ----------------------------------------

        # ==========================================================
        # BACKSPACE
        #
        # Delete the character immediately before the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Helo"
        # cursor  = 2
        # display = "He|lo"
        #
        # ---------------- ANSWER ----------------

        elif key in (8, 127, curses.KEY_BACKSPACE):

            if cursor > 0:
                text = text[0:cursor-1] + text[cursor:]
                cursor -= 1
            

        # ----------------------------------------

        # ==========================================================
        # ENTER
        #
        # Insert a newline at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hel\nlo"
        # cursor  = 4
        # display = "Hel\n|lo"
        #
        # ---------------- ANSWER ----------------

        elif key == 10:

            text = text[0:cursor] + "\n" + text[cursor:]
            cursor += 1


        # ----------------------------------------

        # ==========================================================
        # INSERT CHARACTER
        #
        # Insert the typed character at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # Typing X
        #
        # After
        # text    = "HelXlo"
        # cursor  = 4
        # display = "HelX|lo"
        #
        # ---------------- ANSWER ----------------

        elif 32 <= key <= 126:

            text = text[0:cursor] + chr(key) + text[cursor:]
            cursor += 1

        # ----------------------------------------

        #BONUS: Can you figure out how to select one line up/down by yourself?

        elif key == curses.KEY_UP:
            pos = cursor
            while pos > 0 and text[pos-1] != "\n":
                pos -= 1
            if pos == 0:
                continue
            x = cursor-pos 
            pos -= 1
            x2 = 0
            while pos > 0 and text[pos-1] != "\n":
                pos -= 1
                x2 += 1
            cursor = pos+min(x, x2)
            


        elif key == curses.KEY_DOWN:

            pos = cursor
            while pos > 0 and text[pos-1] != "\n":
                pos -= 1
            x = cursor-pos 
            pos = cursor
            while pos < len(text) and text[pos-1] != "\n":
                pos += 1
            if pos == len(text):
                continue
            x2 = 0
            while pos < len(text) and text[pos] != "\n":
                pos += 1
                x2 += 1
            cursor = pos-x2+min(x, x2)


curses.wrapper(main)
