from turtle import Turtle, Screen
import os, time, random

def clear_terminal():
    os.system("cls" if os.name == 'nt' else "clear")

def sleep(second):
    time.sleep(second)

clear_terminal()
RACERS_LIST = []
colors = ("green", "white", "red")
positions = ((-385,0), (-385, 200 ), (-385, -200))
angles = ((-350,-320), (-350, 320), (330, 320), (330,-320))
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


WINDOW = Screen()
WINDOW.title("Turtle race!")
WINDOW.bgcolor("DarkBlue")
WINDOW.setup(width= 800, height= 800)
WINDOW.tracer(0)

def creat_racers():

    for i in range(3):
        turt = Turtle("turtle")
        turt.penup()
        turt.color(colors[i])
        turt.goto(positions[i])
        RACERS_LIST.append(turt)

def move_racers():
    "Moves turtles and returns color of winner"

    for racer in RACERS_LIST:
        racer.showturtle()
        racer.forward(random.choice((5,8)))

        if racer.xcor() > 380:
            return racer.pencolor()
        
        WINDOW.update()

def hideracers():
    for turt in RACERS_LIST:
        turt.hideturtle()

def print_result(winner_color, choiced_color):
    sleep(3)

    hideracers()
    massage = Turtle()
    massage.hideturtle()
    massage.goto(0,0)
    massage.color('white')

    Arabic_colors =  ["أبيض", "أخضر","أحمر"]
    
    if choiced_color in  Arabic_colors:
        
        if choiced_color == Arabic_colors[0]:
            choiced_color = 'white'

        if choiced_color == Arabic_colors[1]:
            choiced_color = 'green'

        if choiced_color == Arabic_colors[2]:
            choiced_color = 'red'


    if choiced_color.lower() != winner_color:

        WINDOW.bgcolor("red")
        massage.write(f"You lost! 😔 💔 🥹 🤝 \n\n", align="center", font= ("Source Sans Pro", 20, "normal"))
        massage.write(f" 😔 💔 🥹 🤝 لقد خسرت", align="center", font= ("Source Sans Pro", 20, "normal"))

    else:
        massage.write(f"Congratulation you win! 😁😄☺️🎈🎉🥳💃\n\n ", align="center", font= ("Source Sans Pro", 20, "italic"))
        massage.write(f"😁😄☺️🎈🎉🥳💃مبروك، لقد فزت ", align="center", font= ("Source Sans Pro", 20, "italic"))

        for _ in range(10):
            sleep(0.08)
            WINDOW.bgcolor(random.choice(named_colors))
    
    massage.penup()
    massage.color("green1")

    # Print turtles on screen!
    for i in range(4):
        massage.goto(angles[i])
        massage.pendown()
        # massage.write(f"🐢",font=("arial", 40, "bold"))
        
    massage.goto(angles[0])
    WINDOW.update()
    sleep(5)
    massage.clear()
    # massage.clear()

def user_color_choice():
    color_choice = WINDOW.textinput("Choose a color of your racer!", "Enter color of racer: [White, Red, Green]\n\nأكتب لون المتسابق الخاص بك [أبيض، أخضر، أحمر]")
    t = Turtle()
    t.color("white")
    t.hideturtle()

    while str( color_choice ).lower() not in ["white", "red", "green", "أبيض" ,"أخضر" ,"أحمر"]:

        t.write("Enter a correct name!\n\nأدخل اسم صحيح!", align= 'center', font= ("Source Sans Pro", 20, 'normal'))
        WINDOW.update()
        sleep(3)
        t.clear()
        color_choice = WINDOW.textinput("Shoose Color!", "Enter color of racer: [White, Red, green]\n\nأكتب لون المتسابق الخاص بك [أبيض، أخضر، أحمر]")
        WINDOW.update()

    return color_choice

def main():

    global RACERS_LIST
    creat_racers()
    choice_color = user_color_choice()

    race_on = True
    while race_on:
        sleep(0.05)
        winner_color = move_racers()

        if winner_color:
            print_result(winner_color,choice_color)
            race_on = False

    RACERS_LIST = []
    WINDOW.clear()
    WINDOW.bgcolor("DarkBlue")
    WINDOW.tracer(0)

main()

while str (WINDOW.textinput("Play a new game? ", "Enter { Y } to plya a new game!\nاكتب [نعم] إذا أردت اللاعب مرة أخرى ")).lower() in ["y", "نعم"]:
    main()

turt = Turtle()
turt.color("white")
turt.write("GOOD --- BYE!", align="center", font= ("Source Sans Pro", 30, "bold"))

WINDOW.mainloop()