
# This module creates a simple turtle racing game using the turtle graphics
# library. The player chooses a racer color, turtles race across the screen,
# and the game displays a win/lose result. Utility functions handle terminal
# clearing and sleeping used during textual prompts and pacing.


from turtle import Turtle, Screen
import os, time, random


# Clear terminal depending on the operating system
def clear_terminal():
    """
    Clear the terminal/console screen.

    Uses the OS-specific clear command"""

    os.system("cls" if os.name == 'nt' else "clear")

# Small wrapper around time.sleep for clearer calls in the code
def sleep(second):
    """
    Pause execution for a given number of seconds.

    Parameters:
    - second (float): Number of seconds to sleep.
    """
    time.sleep(second)

# Clear the terminal once when the program starts
clear_terminal()

# Global list to store the Turtle racer objects
RACERS_LIST = []

# Predefined visible colors for the three racers
colors = ("green", "white", "red")

# Starting positions for the three racers (x, y)
positions = ((-385,0), (-385, 200 ), (-385, -200))

# Positions/angles used later to display results or emojis
angles = ((-350,-320), (-350, 320), (330, 320), (330,-320))

# A list of many named colors used for celebration background flashing
named_colors = [
    "AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure",
    "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue",
    "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse",
    "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson",
    "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray",
    "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen",
    "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon",
    "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkTurquoise",
    "DarkViolet", "DeepPink", "DeepSkyBlue"
]

# Setup the main Turtle screen/window
window = Screen()
window.title("Turtle race!")
window.bgcolor("DarkBlue")
window.setup(width= 800, height= 800)
window.tracer(0)

# Create three Turtle racers and place them at the starting positions
def create_racers():
    """
    Create and position the racer Turtle objects.

    Behavior:
    - Creates three Turtle instances shaped like a turtle.
    - Lifts their pens (penup) so they don't draw while being moved to  start.
    - Assigns each turtle a color from the global 'colors' tuple.
    - Moves each turtle to a start position from the global 'positions' tuple.
    - Appends each Turtle to the global RACERS_LIST.
    """

    for i in range(3):
        turt = Turtle("turtle")
        turt.penup()
        turt.color(colors[i])
        turt.goto(positions[i])
        RACERS_LIST.append(turt)


# Move each racer forward by a small random step and return the winner's color once a racer crosses the finish line
def move_racers():
    """
    Advance each racer a small random step and check for a winner.

    Behavior:

    - Iterates over every Turtle in RACERS_LIST.
    - Ensures the turtle is visible (showturtle).
    - Moves it forward by a random choice of 5 or 8 pixels.
    - After moving a racer, checks if its x-coordinate exceeds the finish threshold (380).
      If so, returns that racer's pencolor (string) as the winner.
    - Calls WINDOW.update() after moving each racer to refresh the animation.

    Returns:
    - The winner's color as a lowercase/Arabic registered color string if a racer crosses the finish line.
    - None if no racer has yet crossed the finish line.
    """

    for racer in RACERS_LIST:
        racer.showturtle()
        racer.forward(random.choice((5,8)))

        # If the racer crosses the right edge (finish line), return its color as the winner
        if racer.xcor() > 380:
            return racer.pencolor()
        
        # Update screen after moving each racer so animation is visible
        window.update()


# Hide all racer turtles (used when showing the result screen)
def hideracers():
    """
    Hide all racer Turtle objects.

    Behavior:
    - Iterates over RACERS_LIST and calls hideturtle() on each item.
    """ 
    for turt in RACERS_LIST:
        turt.hideturtle()

# Show the race result, compare chosen color with winner, and animate/print messages
def print_result(winner_color, choiced_color):
    """
    Display the race result and celebratory or losing animation.

    Parameters:
    - winner_color (str): The color string of the winning turtle (as returned by move_racers).
    - choiced_color (str): The player's chosen color (may be in English or Arabic).

    Behavior:
    - Waits briefly, hides racers, and creates a hidden writer Turtle to display messages.
    - Accepts Arabic color input by mapping Arabic color words ['أبيض','أخضر','أحمر'] to
      English names ['white', 'green', 'red'].

    - Compares the normalized player choice to the winner color:
        - If they do not match: changes the background to red and writes losing messages
          in both English if choice was english or  else Arabic.
        - If they match: writes winning messages in English or Arabic 
          it depends on the input language, and flashes the
          background with random named colors to celebrate.

    - Optionally positions the message turtle in a few corners/angles (angles global).
    - Sleeps to let the player read the result then clears the message.
    """

    sleep(3)

    hideracers()
    massage = Turtle()
    massage.hideturtle()
    massage.goto(0,0)
    massage.color('white')

    # Arabic color names that the user may input — used to accept Arabic input
    Arabic_colors =  ["أبيض", "أخضر","أحمر"]
    
    is_arabic = False

    if choiced_color in  Arabic_colors:
        is_arabic = True

        if choiced_color == Arabic_colors[0]:
            choiced_color = 'white'

        if choiced_color == Arabic_colors[1]:
            choiced_color = 'green'

        if choiced_color == Arabic_colors[2]:
            choiced_color = 'red'

    # Compare chosen color (normalized to lowercase) with the winner color
    if choiced_color != winner_color:

        window.bgcolor("red") # change the background to red

        # Write losing messages in Arabic if the input was Arabic
        if is_arabic:

            massage.write(f" 😔 💔 🥹 🤝 لقد خسرت", align="center", font= ("Source Sans Pro", 20, "normal"))

        # else write losing messages in English
        else:
            massage.write(f"You lost! 😔 💔 🥹 🤝 \n\n", align="center", font= ("Source Sans Pro", 20, "normal"))

    else:

        # Write winning messages in Arabic if the input was Arabic
        if is_arabic:

            massage.write(f"😁😄☺️🎈🎉🥳💃مبروك، لقد فزت ", align="center", font= ("Source Sans Pro", 20, "italic"))

        # else write winning messages in English
        else:
            massage.write(f"Congratulation you win! 😁😄☺️🎈🎉🥳💃\n\n ", align="center", font= ("Source Sans Pro", 20, "italic"))

        # Celebration: flash the background with random named colors
        for _ in range(10):
            sleep(0.08)
            window.bgcolor(random.choice(named_colors))


    # Prepare to draw small symbols (or position text) around the screen
    massage.penup()
    massage.color("green1")

    # Print turtles on screen!
    for i in range(4):
        massage.goto(angles[i])
        massage.pendown()
        
    # Return the writer to the first angle and update the screen
    massage.goto(angles[0])
    window.update()

    sleep(5)

    massage.clear() # clear the messages before proceeding

# Ask the user to choose a color for their racer using a dialog; validate input (English or Arabic)
def user_color_choice():

    """
    Prompt the player to choose a racer color using a dialog and validate the input.

    Behavior:
    - Opens a text input dialog (window.textinput) asking the user to type one of:

      'White', 'Red', 'Green' or the Arabic equivalents 'أبيض', 'أخضر', 'أحمر'.

    - If the entered value is not in the accepted set, displays an on-screen message
      asking for a correct name, waits, clears the message, and repeats the prompt.
    - Continues looping until a valid choice is entered.

    Returns:
    - The raw string returned by textinput (the user's choice). This may be an Arabic
      or English color word; callers usually normalize or map Arabic to English.
    """
     
    # Ask the racer color input in English or Arabic
    color_choice = window.textinput("Choose a color of your racer!", "Enter color of racer: [White, Red, Green]\n\nأكتب لون المتسابق الخاص بك [أبيض، أخضر، أحمر]")


    t = Turtle()
    t.color("white")
    t.hideturtle()

    if str( color_choice ).lower() not in ["white", "red", "green"] and color_choice not in ["أبيض" ,"أخضر" ,"أحمر"]:

        # Keep prompting until the user enters one of the accepted color names (English or Arabic)
        while True:

            # Hide reacer from screen!
            hideracers()

            # show massage if the input color names incorrect
            t.write("Enter a correct name!\n\nأدخل اسم صحيح", align= 'center', font= ("Source Sans Pro", 20, 'normal'))

            window.update()

            sleep(3)

            t.clear()

            # Ask the racer color input in English or Arabic
            color_choice = window.textinput("Shoose Color!", "Enter color of racer: [White, Red, Green]\n\nأكتب لون المتسابق الخاص بك [أبيض، أخضر، أحمر]")

            window.update()
            if str( color_choice ).lower() in ["white", "red", "green"] or color_choice in ["أبيض" ,"أخضر" ,"أحمر"]:
                break


    # return the chooiced color as Arabic
    if color_choice in ["أبيض" ,"أخضر" ,"أحمر"]:

        return color_choice
    
    # return the chooiced color as lowercase if the input is English 
    else:
        return str(color_choice).lower()

# Main function to initialize racers, run the race loop, and show results
def main():

    """
    Initialize a race, run it until a winner is determined, and show the result.

    Behavior:
    - Calls creat_racers to instantiate and position the three racer Turtles.
    - Prompts the user for their racer color via user_color_choice.
    - Enters a loop that repeatedly calls move_racers with a short sleep between frames
      until move_racers returns a winner color.
    - Calls print_result with the winner color and the player's choice to display the outcome.
    - Resets global state (RACERS_LIST) and clears the (window) so the game can be replayed.
    """

    global RACERS_LIST

    create_racers() # create and position the three racers

    # get the user's chosen racer color
    choice_color = user_color_choice()

    # game state
    race_on = True

    while race_on:

        # short delay to control animation speed
        sleep(0.05)

        # advance racers and see if there is a winner
        winner_color = move_racers()

        # When move_racers returns a color, a racer won; show result and stop the race
        if winner_color:
            print_result(winner_color,choice_color)

            race_on = False

    # Reset state for a potential new game
    RACERS_LIST = []
    window.clear()
    window.bgcolor("DarkBlue")
    window.tracer(0)


# Start the first game
main()

# Initialize a turtle to asking for a new game
turt = Turtle()
turt.color("white")
turt.hideturtle()

# Offer to play again: prompt with a dialog and loop while user answers yes (English "y" or Arabic "نعم")
while True:

    # Ask for a new game in English or Arabic
    new_game = str (window.textinput("Play a again? ", "Enter [ Y ] to start a new game! or [ N ] to exit\nإذا أردت اللعب مرة أخرى اكتب [ نعم ] أو [ لا ]  للخروج ")).lower()

    # Check input if wants a new game start game
    if new_game in ["y", "نعم"]:
        main()

    # Check if input negative stop looping
    elif new_game in ["n", "لا"]:
        break

    # Check if the input not acceptable show incorrect massage
    else:
        turt.write(f"Entry [ {new_game} ] is incorrect!", align="center", font= ("Source Sans Pro", 30, "bold"))
        window.update()
        sleep(3)
        turt.clear()

# Final goodbye message written on the screen
turt.write("GOOD --- BYE!", align="center", font= ("Source Sans Pro", 30, "bold"))

window.mainloop()